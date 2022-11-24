from download import download
format = ["zip","tar","file","tar.gz"]
while True :
    url = input("please Enter donload link : ")
    link = download(url,"file",replace=True)
    print("============================\nyour file downloaded \n============================\n")
    
