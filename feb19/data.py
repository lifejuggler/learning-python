import pymongo
import random

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
print(myclient.list_database_names())

mydb = myclient["mydatabase"]

collist = mydb.list_collection_names()
customers_col = mydb["customers"]
if "customers" in collist:
  print("The collection exists.")
else:
  x = customers_col.insert_many([{"id":1,"first_name":"Lon","last_name":"Kennedy","email":"lkennedy0@printfriendly.com","gender":"Male","points":83877,"country":"United States"},
  {"id":2,"first_name":"Averell","last_name":"Gollin","email":"agollin1@liveinternet.ru","gender":"Male","points":92552,"country":"Canada"},
  {"id":3,"first_name":"Reamonn","last_name":"Durn","email":"rdurn2@theglobeandmail.com","gender":"Male","points":54191,"country":"France"},
  {"id":4,"first_name":"Mata","last_name":"Meuse","email":"mmeuse3@umn.edu","gender":"Male","points":17222,"country":"France"},
  {"id":5,"first_name":"Steven","last_name":"Prevett","email":"sprevett4@ow.ly","gender":"Genderfluid","points":78289,"country":"United States"},
  {"id":6,"first_name":"Keefe","last_name":"Rivallant","email":"krivallant5@jugem.jp","gender":"Male","points":43125,"country":"United States"},
  {"id":7,"first_name":"Gilberte","last_name":"Edgar","email":"gedgar6@smugmug.com","gender":"Female","points":47197,"country":"United States"},
  {"id":8,"first_name":"Melisande","last_name":"Leete","email":"mleete7@furl.net","gender":"Female","points":91881,"country":"Australia"},
  {"id":9,"first_name":"Jereme","last_name":"Kornalik","email":"jkornalik8@hostgator.com","gender":"Male","points":85948,"country":"Mexico"},
  {"id":10,"first_name":"Lexis","last_name":"Bluschke","email":"lbluschke9@wordpress.org","gender":"Female","points":63728,"country":"Mexico"},
  {"id":11,"first_name":"Filippo","last_name":"Gilhool","email":"fgilhoola@abc.net.au","gender":"Male","points":97245,"country":"United States"},
  {"id":12,"first_name":"Harcourt","last_name":"Polotti","email":"hpolottib@bloglines.com","gender":"Male","points":59908,"country":"Canada"},
  {"id":13,"first_name":"Ruthy","last_name":"Taffee","email":"rtaffeec@goo.gl","gender":"Female","points":66202,"country":"France"},
  {"id":14,"first_name":"Augy","last_name":"Marsland","email":"amarslandd@shinystat.com","gender":"Male","points":2110,"country":"France"},
  {"id":15,"first_name":"Issiah","last_name":"Stringfellow","email":"istringfellowe@dedecms.com","gender":"Male","points":18668,"country":"France"},
  {"id":16,"first_name":"Corney","last_name":"Loosmore","email":"cloosmoref@wufoo.com","gender":"Male","points":50378,"country":"United States"},
  {"id":17,"first_name":"Gordan","last_name":"Milnthorpe","email":"gmilnthorpeg@upenn.edu","gender":"Male","points":63371,"country":"United States"},
  {"id":18,"first_name":"Rochelle","last_name":"Dahlman","email":"rdahlmanh@netlog.com","gender":"Female","points":29360,"country":"Canada"},
  {"id":19,"first_name":"Demetri","last_name":"O'Bradane","email":"dobradanei@themeforest.net","gender":"Male","points":73021,"country":"Germany"},
  {"id":20,"first_name":"Aundrea","last_name":"Calder","email":"acalderj@booking.com","gender":"Female","points":84699,"country":"United States"},
  {"id":21,"first_name":"Caz","last_name":"Epps","email":"ceppsk@prnewswire.com","gender":"Male","points":80647,"country":"France"},
  {"id":22,"first_name":"Amargo","last_name":"Towers","email":"atowersl@t.co","gender":"Female","points":58930,"country":"France"},
  {"id":23,"first_name":"Neddie","last_name":"Harrild","email":"nharrildm@ucoz.com","gender":"Male","points":94514,"country":"Canada"},
  {"id":24,"first_name":"Randee","last_name":"Francisco","email":"rfranciscon@icq.com","gender":"Female","points":12443,"country":"Canada"},
  {"id":25,"first_name":"Emily","last_name":"Yanshinov","email":"eyanshinovo@hhs.gov","gender":"Female","points":32704,"country":"United States"},
  {"id":26,"first_name":"Aaren","last_name":"Redmille","email":"aredmillep@trellian.com","gender":"Female","points":62996,"country":"United States"},
  {"id":27,"first_name":"Walther","last_name":"Turney","email":"wturneyq@creativecommons.org","gender":"Male","points":99222,"country":"Canada"},
  {"id":28,"first_name":"Dugald","last_name":"Reame","email":"dreamer@slideshare.net","gender":"Male","points":15278,"country":"France"},
  {"id":29,"first_name":"Willem","last_name":"Stores","email":"wstoress@gov.uk","gender":"Male","points":47726,"country":"France"},
  {"id":30,"first_name":"Perry","last_name":"Parnham","email":"pparnhamt@oaic.gov.au","gender":"Male","points":56319,"country":"United States"},
  {"id":31,"first_name":"Stevy","last_name":"Matten","email":"smattenu@istockphoto.com","gender":"Polygender","points":94549,"country":"Canada"},
  {"id":32,"first_name":"Ileane","last_name":"Clementucci","email":"iclementucciv@nifty.com","gender":"Female","points":98599,"country":"United States"},
  {"id":33,"first_name":"Glennis","last_name":"Garci","email":"ggarciw@japanpost.jp","gender":"Genderqueer","points":97413,"country":"Canada"},
  {"id":34,"first_name":"Edmon","last_name":"Palfreman","email":"epalfremanx@harvard.edu","gender":"Male","points":46467,"country":"France"},
  {"id":35,"first_name":"Stephi","last_name":"Doudney","email":"sdoudneyy@accuweather.com","gender":"Female","points":44505,"country":"Mexico"},
  {"id":36,"first_name":"Ronny","last_name":"O'Brallaghan","email":"robrallaghanz@techcrunch.com","gender":"Male","points":58137,"country":"France"},
  {"id":37,"first_name":"Chlo","last_name":"Iamittii","email":"ciamittii10@baidu.com","gender":"Female","points":9582,"country":"France"},
  {"id":38,"first_name":"Raquel","last_name":"Bretherick","email":"rbretherick11@yellowbook.com","gender":"Female","points":52786,"country":"Mexico"},
  {"id":39,"first_name":"Tressa","last_name":"Kleinfeld","email":"tkleinfeld12@howstuffworks.com","gender":"Female","points":27664,"country":"France"},
  {"id":40,"first_name":"Edeline","last_name":"Arendt","email":"earendt13@ox.ac.uk","gender":"Female","points":2311,"country":"Mexico"},
  {"id":41,"first_name":"Marin","last_name":"Gainsford","email":"mgainsford14@vk.com","gender":"Female","points":64096,"country":"France"},
  {"id":42,"first_name":"Adelind","last_name":"Wince","email":"awince15@ucla.edu","gender":"Female","points":70713,"country":"France"},
  {"id":43,"first_name":"Talia","last_name":"Wimmer","email":"twimmer16@wufoo.com","gender":"Female","points":86837,"country":"Canada"},
  {"id":44,"first_name":"Kent","last_name":"Longhirst","email":"klonghirst17@tripadvisor.com","gender":"Male","points":18353,"country":"Canada"},
  {"id":45,"first_name":"Chanda","last_name":"Wurst","email":"cwurst18@e-recht24.de","gender":"Female","points":97143,"country":"France"},
  {"id":46,"first_name":"Lori","last_name":"Robjents","email":"lrobjents19@theglobeandmail.com","gender":"Female","points":55271,"country":"Mexico"},
  {"id":47,"first_name":"Carce","last_name":"Ownsworth","email":"cownsworth1a@columbia.edu","gender":"Male","points":81781,"country":"United States"},
  {"id":48,"first_name":"Arlen","last_name":"Ricardo","email":"aricardo1b@weebly.com","gender":"Female","points":34348,"country":"France"},
  {"id":49,"first_name":"Clem","last_name":"Lethbridge","email":"clethbridge1c@163.com","gender":"Female","points":45728,"country":"France"},
  {"id":50,"first_name":"Jay","last_name":"Smithe","email":"jsmithe1d@twitter.com","gender":"Male","points":54020,"country":"Canada"},
  {"id":51,"first_name":"Forest","last_name":"Walsh","email":"fwalsh1e@addtoany.com","gender":"Male","points":15040,"country":"France"},
  {"id":52,"first_name":"Gregor","last_name":"Lippiatt","email":"glippiatt1f@photobucket.com","gender":"Male","points":32044,"country":"Australia"},
  {"id":53,"first_name":"Berkie","last_name":"Poxton","email":"bpoxton1g@blinklist.com","gender":"Male","points":79120,"country":"France"},
  {"id":54,"first_name":"Stinky","last_name":"Hudel","email":"shudel1h@reference.com","gender":"Male","points":72159,"country":"United States"},
  {"id":55,"first_name":"Sibelle","last_name":"Amiable","email":"samiable1i@csmonitor.com","gender":"Genderqueer","points":21045,"country":"United States"},
  {"id":56,"first_name":"Gayelord","last_name":"Forestall","email":"gforestall1j@elegantthemes.com","gender":"Male","points":24316,"country":"Canada"},
  {"id":57,"first_name":"Tawnya","last_name":"Albrooke","email":"talbrooke1k@gov.uk","gender":"Female","points":77976,"country":"United States"},
  {"id":58,"first_name":"Conant","last_name":"Langtree","email":"clangtree1l@issuu.com","gender":"Male","points":55705,"country":"United States"},
  {"id":59,"first_name":"Seamus","last_name":"Pedder","email":"spedder1m@howstuffworks.com","gender":"Male","points":95302,"country":"France"},
  {"id":60,"first_name":"Brnaby","last_name":"Barbie","email":"bbarbie1n@surveymonkey.com","gender":"Male","points":75586,"country":"France"},
  {"id":61,"first_name":"Betsey","last_name":"Ottam","email":"bottam1o@digg.com","gender":"Female","points":27584,"country":"Canada"},
  {"id":62,"first_name":"Sherwynd","last_name":"Lockitt","email":"slockitt1p@ca.gov","gender":"Male","points":97909,"country":"France"},
  {"id":63,"first_name":"Loralee","last_name":"Leveritt","email":"lleveritt1q@marriott.com","gender":"Female","points":71049,"country":"France"},
  {"id":64,"first_name":"Madelyn","last_name":"Rexworthy","email":"mrexworthy1r@phoca.cz","gender":"Agender","points":373,"country":"Canada"},
  {"id":65,"first_name":"Nicolai","last_name":"Ottery","email":"nottery1s@mail.ru","gender":"Male","points":29162,"country":"France"},
  {"id":66,"first_name":"Gaylor","last_name":"Geach","email":"ggeach1t@sogou.com","gender":"Male","points":96700,"country":"France"},
  {"id":67,"first_name":"Traver","last_name":"Hush","email":"thush1u@scientificamerican.com","gender":"Male","points":29917,"country":"Mexico"},
  {"id":68,"first_name":"Ellerey","last_name":"Itzkowicz","email":"eitzkowicz1v@answers.com","gender":"Male","points":65463,"country":"France"},
  {"id":69,"first_name":"Noni","last_name":"Chattell","email":"nchattell1w@digg.com","gender":"Female","points":2919,"country":"United States"},
  {"id":70,"first_name":"Byrom","last_name":"Gipp","email":"bgipp1x@ucla.edu","gender":"Genderfluid","points":82083,"country":"France"},
  {"id":71,"first_name":"Bartholomew","last_name":"Pullin","email":"bpullin1y@xrea.com","gender":"Male","points":51044,"country":"France"},
  {"id":72,"first_name":"Horatia","last_name":"Feavers","email":"hfeavers1z@psu.edu","gender":"Female","points":71337,"country":"France"},
  {"id":73,"first_name":"Urson","last_name":"Veschi","email":"uveschi20@msu.edu","gender":"Male","points":11580,"country":"Canada"},
  {"id":74,"first_name":"Merwin","last_name":"Hovey","email":"mhovey21@wikia.com","gender":"Male","points":47832,"country":"France"},
  {"id":75,"first_name":"Woodie","last_name":"Yoselevitch","email":"wyoselevitch22@storify.com","gender":"Male","points":84733,"country":"France"},
  {"id":76,"first_name":"Theodosia","last_name":"Martill","email":"tmartill23@addtoany.com","gender":"Female","points":57862,"country":"United States"},
  {"id":77,"first_name":"Benji","last_name":"Matterface","email":"bmatterface24@dailymotion.com","gender":"Male","points":77324,"country":"Mexico"},
  {"id":78,"first_name":"Ingrid","last_name":"Horsted","email":"ihorsted25@is.gd","gender":"Genderfluid","points":19569,"country":"United States"},
  {"id":79,"first_name":"Kennith","last_name":"Paull","email":"kpaull26@hatena.ne.jp","gender":"Male","points":60195,"country":"United States"},
  {"id":80,"first_name":"Hurley","last_name":"Kewzick","email":"hkewzick27@arstechnica.com","gender":"Male","points":1702,"country":"Canada"},
  {"id":81,"first_name":"Erie","last_name":"Rainon","email":"erainon28@weebly.com","gender":"Male","points":20361,"country":"France"},
  {"id":82,"first_name":"Clayton","last_name":"Grevatt","email":"cgrevatt29@blogger.com","gender":"Male","points":38168,"country":"France"},
  {"id":83,"first_name":"Lidia","last_name":"Paulazzi","email":"lpaulazzi2a@fotki.com","gender":"Female","points":16993,"country":"France"},
  {"id":84,"first_name":"Linette","last_name":"Tunn","email":"ltunn2b@vinaora.com","gender":"Female","points":28264,"country":"United Kingdom"},
  {"id":85,"first_name":"Randi","last_name":"Rushworth","email":"rrushworth2c@hatena.ne.jp","gender":"Male","points":2208,"country":"United States"},
  {"id":86,"first_name":"Missy","last_name":"Birchill","email":"mbirchill2d@devhub.com","gender":"Female","points":72302,"country":"United States"},
  {"id":87,"first_name":"Avrom","last_name":"Heales","email":"aheales2e@mediafire.com","gender":"Male","points":36366,"country":"United States"},
  {"id":88,"first_name":"Sofia","last_name":"Gwioneth","email":"sgwioneth2f@list-manage.com","gender":"Female","points":17295,"country":"France"},
  {"id":89,"first_name":"Sheff","last_name":"McGeaney","email":"smcgeaney2g@hatena.ne.jp","gender":"Genderqueer","points":42729,"country":"France"},
  {"id":90,"first_name":"Perle","last_name":"Ambrogioni","email":"pambrogioni2h@cisco.com","gender":"Female","points":14615,"country":"Mexico"},
  {"id":91,"first_name":"Norby","last_name":"Rowbrey","email":"nrowbrey2i@hp.com","gender":"Male","points":45044,"country":"South Korea"},
  {"id":92,"first_name":"Diannne","last_name":"Heddan","email":"dheddan2j@istockphoto.com","gender":"Female","points":73276,"country":"France"},
  {"id":93,"first_name":"Doyle","last_name":"Thewys","email":"dthewys2k@people.com.cn","gender":"Male","points":82025,"country":"United States"},
  {"id":94,"first_name":"Carolin","last_name":"McCritichie","email":"cmccritichie2l@hatena.ne.jp","gender":"Female","points":93613,"country":"Canada"},
  {"id":95,"first_name":"Ofilia","last_name":"Korejs","email":"okorejs2m@wikimedia.org","gender":"Female","points":17952,"country":"Mexico"},
  {"id":96,"first_name":"Alvy","last_name":"Smiths","email":"asmiths2n@yahoo.com","gender":"Male","points":42721,"country":"France"},
  {"id":97,"first_name":"Demott","last_name":"Flancinbaum","email":"dflancinbaum2o@ehow.com","gender":"Male","points":38031,"country":"Canada"},
  {"id":98,"first_name":"Lanna","last_name":"Colebrook","email":"lcolebrook2p@quantcast.com","gender":"Polygender","points":46831,"country":"United States"},
  {"id":99,"first_name":"Bernice","last_name":"Ledrun","email":"bledrun2q@cbslocal.com","gender":"Female","points":17445,"country":"Mexico"},
  {"id":100,"first_name":"Ertha","last_name":"Cescotti","email":"ecescotti2r@accuweather.com","gender":"Female","points":20988,"country":"Canada"}])
  print(x.inserted_ids)

all_customers = customers_col.find()
points_col = mydb["points"]
if not "points" in collist:
  to_insert = []
  idx = 1
  for c in all_customers:
    to_insert.append({'id': idx, 'country': c['country'], 'points': random.randint(100, 100000)})
  y = points_col.insert_many(to_insert)