from download import download
while True :
    url = input("please Enter donload link : ")
    link = download(url,"file",replace=True)
    print("============================\nyour file downloaded \n============================\n")
