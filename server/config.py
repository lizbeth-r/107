import pymongo
import certifi
con_str = "mongodb+srv://aglaeramirez266:kale123@cluster0.kjacf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db=client.get_database("organika")
