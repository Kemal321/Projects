###################################################################
# "dasal_rotation"
###################################################################
# @Description: "İki frame arasında ki özellikleri eşleyerek ve bu özellik noktalarını mesafeye göre sıralayarak 
#                %x lik bir kısımları arasında bir lineer doğru çıkarımı yapılmaktadır. Knn kümeleme yöntemi ile. 
#                Bu doğruların birbirine olan açıları ile iki frame arası dönme farkını yaklaşımsal olarak bulmaktadır."
#  @Note : "Framelerin resize değeri, noktaların % kaçlık kısımlarının alınacağının ve feature dedectior'un parametlerine
#           dikkat edilmedilir. Bu parametreler algoritmanın yaklaşımsal sonuç değerinde önemli yere sahiptir. "


#   Version 0.0.1:  "Feature Dedection ve İlgili alanların sınıflandırılması "
#                   ...
#                   02 AĞUSTOS 2022 Sal, 13:00 - "Fatih HAŞLAK,Mucahid KARAAGAC"
#   Version 0.0.2:  "İlgili alanların kordinat sisteminde nokta olarak belirtilip
#                    en uygun line bulunması ve tüm noktaların mın max'ında ki açı değerinin
#                    yaklaşıksal olarak hesaplanması"
#                   ...
#                   3 Ağustos 2022 Çar, 08:00 - "Fatih HAŞLAK,Mucahid KARAAGAC"

#   Version 0.0.3:  ""
#                   ...
#                    Ağustos 2022 , 08:30 - "Fatih HAŞLAK,Mucahid KARAAGAC"
 

import math
import cv2 #version  >= 4.5.1
import numpy as np #version >=1.21.5
from skimage.measure import ransac,LineModelND
from shapely.geometry import Point #version 1.8.4 last version
from shapely.geometry import LineString

buffer_length=10
list_of_degree=[]
counter_degree=0

def video_frame(cap,frame):
  
  while(True):
  

    try:
      _,frame1=cap.read()#frame2
             
      frame1 = frame1[240:840,660:1260] 
      
      chos=frame#frame1
      
      cho=frame1.copy()

      frame=frame1.copy()#frame2
        
      hesapla(chos,cho)
    except:
      print("HATA!!!!!")
    
    


def hesapla(chos,cho):
  global buffer_length
  global list_of_degree
  global counter_degree

  dedector = cv2.ORB_create(nfeatures = 10000) #Orb feature dedector olusturucu
  descriptor = cv2.xfeatures2d.BEBLID_create(0.75)
  kpts1 = dedector.detect(chos, None)
  kpts2 = dedector.detect(cho, None)
  kp1, des1 = descriptor.compute(chos, kpts1)
  kp2, des2 = descriptor.compute(cho, kpts2)

  bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True) #brute force matcher ile noktaları eşleştirme
  matches = bf.match(des1, des2) #eşlenmiş noktalar


  good_matches=[]

  good_matches = sorted(matches, key = lambda x: x.distance) #mesafeye göre sırala
  good_matches=good_matches[:int(len(good_matches)/2)]
  src_pts = np.float32([ kp1[match.queryIdx].pt for match in good_matches ] ).reshape(-1, 2) #source image pointler x,y
  dst_pts = np.float32([ kp2[match.trainIdx].pt  for match in good_matches ] ).reshape(-1, 2) #hedef image pointler x1,y1



  list_p1=[]
  list_p2=[]

  for point in src_pts: #source pointlerimin inlier noktalarını al ve list_p1'e at.
    list_p1.append((point[0],point[1]))
  for point in dst_pts:  #hedef pointlerimin inlier noktalarını al ve list_p2'e at.
    list_p2.append((point[0],point[1]))


  lenght=int(len(list_p1))
  if(lenght<1200):
    print("Ayni Konumda Degil")

  #else konulabilir ????
  


  point_p1=list_p1[0:][0:] #point p1 in içine at ve arraye çevir
  point_p2=list_p2[0:][0:] #point p1 in içine at ve arraye çevir

  point_p1=np.array(point_p1).astype(np.float64)
  point_p2=np.array(point_p2).astype(np.float64)


  x=point_p1[0:,0] # 1.fonksiyonun x datası
  y=600-point_p1[0:,1] # 1.fonskyionun y datası (İNTvalues=shape)

  x1=point_p2[0:,0] # 2.fonksiyonun x datası
  y1=600-point_p2[0:,1] #2.fonksyıonun y datası


  data =np.column_stack([x, y])
  data2 = np.column_stack([x1, y1])
  


  model_robust, inliers = ransac(data, LineModelND, min_samples=int(len(data)*0.5), 
                                residual_threshold=40  , max_trials=1000,random_state=42,stop_probability=1)

  
  model_robust2, inliers2 = ransac(data2, LineModelND, min_samples=int(len(data)*0.5),
                                residual_threshold=40, max_trials=1000,random_state=42,stop_probability=1)


  line_y_robust = model_robust.predict_y(x)


  line_y_robust2 = model_robust2.predict_y(x1)

  

  indeks=np.where(inliers==True)
  indeks2=np.where(inliers2==True)
  indeks=indeks[0]
  indeks2=indeks2[0]
  indeks=set(list(indeks))
  indeks2=set(indeks2)
  depo=list(indeks.intersection(list(indeks2)))
  
  
  ### baslangıc 1.line

  point = Point(x[depo[0]], y[depo[0]])
  line1=LineString( [ (min(x),line_y_robust[np.argmin(x)]),(max(x),line_y_robust[np.argmax(x)]) ])

  dist =line1.project(point)
  
  baslangic=list(line1.interpolate(dist).coords)
  ###

  ### bitiş 1.line
  point2=Point(x[depo[-1]], y[depo[-1]])
  
  dist_2 = line1.project(point2)
 
  bitis=list(line1.interpolate(dist_2).coords)
  ######

  # noktanın eğimi
  slope=((baslangic[0][1]) - y[depo[0]])/(baslangic[0][0]-x[depo[0]]) 
  slope2=((bitis[0][1]) - y[depo[-1]])/(bitis[0][0]-x[depo[-1]])
  slope_line=((baslangic[0][1]) - bitis[0][1])/(baslangic[0][0]-bitis[0][0])
  print("Eğim % 2.f " %(slope_line*slope))
  print("Eğim % 2.f " %(slope2*slope_line))
  # 
  ### baslangıc 2.line
  point3=Point(x1[depo[0]], y1[depo[0]])
  line2=LineString( [ (min(x1),line_y_robust2[np.argmin(x1)]),(max(x1),line_y_robust2[np.argmax(x1)])  ])
  dist_3 = line2.project(point3)
  baslangic_1=list(line2.interpolate(dist_3).coords)
  
  ###### bitis 2.line
  point4=Point(x1[depo[-1]], y1[depo[-1]])
  dist_4 =line2.project(point4)
  bitiş_1=list(line2.interpolate(dist_4).coords)
  ######
  #slope_=((baslangic_1[0][1]) - y1[depo[0]])/(baslangic_1[0][0]-x1[depo[0]])
  #slope2_=((bitiş_1[0][1]) - y1[depo[-1]])/(bitiş_1[0][0]-x1[depo[-1]])
 

  nokta_1=baslangic[0]
  nokta_2=bitis[0]
  vector1=np.array([nokta_1,nokta_2])

  nokta_3=baslangic_1[0]
  nokta_4=bitiş_1[0]
  vector2=np.array([nokta_3,nokta_4])
    

  def quadrant(va,degree):
    if(va[0]>0 and va[1]>0):#bölge 1
      return degree
    elif(va[0]>0 and va[1]<0): #bölge 4
      return degree+360
    else:
      return degree+180 #bölge 3


  def ang(point_p1, point_p2):
      # Get nicer vector form
            #inital point x   end point x          inital point y  end point y
      vA = [(point_p1[0,0]-point_p1[1,0]), (point_p1[0,1]-point_p1[1,1])] #(p1 ilk x - p1 son x), (p1 ilk y p1 son y)
      
      #vA type=list  #örnek [31, -98] Rows: 2 
      vB = [(point_p2[0,0]-point_p2[1,0]), (point_p2[0,1]-point_p2[1,1])]  #(p2 ilk x - p2 son x), (p2 ilk y p2 son y)
      
    
      ilk=math.degrees(math.atan(vA[1]/vA[0])) #karşı bölü komşu
      son=math.degrees(math.atan(vB[1]/vB[0]))
    
      degg = (quadrant(vA,ilk) - quadrant(vB,son) ) #quadrant ile bölge tahmini yap ve dereceyi ayarla

      return degg 
  

  deger=ang(vector1,vector2) #fonksiyonu cagır
  print("THE DEGREE -->> {}  ".format(deger))
 
  counter_degree+=deger
  
  if(len(list_of_degree)==buffer_length):
    
    list_of_degree.pop(0)
    list_of_degree.append(deger)
       
  else:
      list_of_degree.append(deger)

  
  print("List of degree",list_of_degree)
  print("Degree Change",counter_degree)
  cv2.putText(chos,str(deger),(10,40),cv2.FONT_HERSHEY_COMPLEX,1.3,(0,0,255))
  cv2.imshow("chos",chos)
  cv2.waitKey(3)
  
  
if __name__=="__main__":
   
    cap = cv2.VideoCapture("Data/20_metre_saat_yönü_drone_sabit.MP4")
   
    
    ret , frame = cap.read()
   
    if(cap.isOpened()):
      frame = frame[240:840,660:1260]
    
      video_frame(cap,frame)

    else:
      print(" The Video Is Can't Opening , Please Check The Adress Of The Video")