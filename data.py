# List of parameters and variables where store the data

list_police_parameters = ["Soruşturma Numarası", "Suç Tipi", "Olay Yeri", "Olay Zamanı", "Şüpheli Sayısı", "Tanık Sayısı", "Polis Memurunun Adı",
                          "Polis Memurunun Soyadı","PM Sicil Numarası","Tanık TCKN","Tanığın Adı","Tanığın Soyadı","Doğum Tarihi","Cinsiyeti","Etnik Kökeni"]

param_esgal_tarifi = "Esgal tarifi"
list_witness_parameters = ["Tanik Adi", "Tanik TCKN", param_esgal_tarifi]
#list_witness_parameters = ["Soruşturma Numarası", "A. TANIK BİLGİLERİ","Tanık TCKN","Tanık Ad","Tanık Soyad","Tanık Cinsiyet","Tanık Doğum Tarihi","Nüfus Kayıt Bilgileri","İkamet Adresi","İletişim Bilgileri","B. OLAY BİLGİLERİ","Olayın mağduru musunuz?","Olaya tanık olduğunuz tarih/saat\nnedir?","Olayı doğrudan gördünüz mü?","Olayı ne kadar süre ile \ngözlemlediniz?","Faile olan uzaklığınız ne kadardı?","Gözlük veya lens kullanıyor \nmusunuz?","Evetse, olay anında kullanıyor \nmuydunuz?","Olay günü bilincinizi etkileyecek \nbir ilaç, madde veya alkol aldınız mı?","Evetse, neydi? Ne zaman ve ne\nkadar kullanmıştınız?","Fiziksel bir şiddet olayına \ntanık oldunuz mu?","Silah kullanıldı mı?","Kullanıldıysa, ne tür bir silah \nkullanıldı?","Olayda size yönelmiş bir tehdit \nveya şiddet eylemi mevcut muydu?","C. FAİL BİLGİLERİ","Faili olay öncesinde tanıyor\n muydunuz?","Şüphelinin resmini teşhis\nişleminden önce gördünüz mü?","Gördüyseniz nerede?\nAranıyor ilanı, gazete, sosyal medya vb.","Şüphelinin robot resminin \nçizilmesine yardımcı  oldunuz mu?",param_esgal_tarifi]

suspect_image_path = ""
f1_image_path = ""
f2_image_path = ""
f3_image_path = ""
f4_image_path = ""
f5_image_path = ""

#dict_witness_parameters = {}
#dict_police_parameters = {}
#final_lineup_list = []

dict_police_parameters = {
    'Soruşturma Numarası: ': '123456789', 'Suç Tipi: ': 'Cinayet', 'Olay Yeri:': 'Tarlabasi',
    'Olay Zamanı:': '12.20.2021', 'Şüpheli Sayısı:': '1', 'Tanık Sayısı: ': '4', 'Polis Memurunun Adı:': 'Nevzat',
    'Polis Memurunun Soyadı:': 'Baskomer', 'PM Sicil Numarası: ': '987654321', 'Tanık TC KN:': '12345678999',
    'Tanığın Adı:': 'Bahattin', 'Tanığın Soyadı: ': 'Kocaman', 'Doğum Tarihi:': '01.01.1970', 'Cinsiyeti': 'Erkek',
    'Etnik Kökeni': 'Türk'
 }
dict_witness_parameters = {'Tanik Adi': 'sdf', 'Tanik TCKN': 'sdf', 'Esgal Tarifi': 'sdf'}
witness_image_choice = "FaceDataset/v3_0868335.jpg"
witness_confidence = "High"

final_lineup_list = ['FaceDataset/v3_0868335.jpg', 'FaceDataset/v3_0495484.jpg', 'FaceDataset/v3_0561451.jpg', 'FaceDataset/v3_0925882.jpg', 'FaceDataset/v3_0169122.jpg']
suspect_image_path = "C:\\Users\\baris\\PycharmProjects\\Eyewitness_Identification_Project\\FaceDataset\\v3_0003928.jpg"
f1_image_path = "FaceDataset/v3_0868335.jpg"
f2_image_path = "C:\\Users\\baris\\PycharmProjects\\Eyewitness_Identification_Project\\GB6\\2.png"
f3_image_path = "C:\\Users\\baris\\PycharmProjects\\Eyewitness_Identification_Project\\GB6\\2.png"
f4_image_path = "C:\\Users\\baris\\PycharmProjects\\Eyewitness_Identification_Project\\GB6\\2.png"
f5_image_path = "C:\\Users\\baris\\PycharmProjects\\Eyewitness_Identification_Project\\\GB6\\2.png"

