from PIL import Image

def createImageList(n):
    for i in range(n):
        path = input("Enter the path of the image (ex F://dir//image.png) : ")
        imageList.append(Image.open(path))

def convertImageList():
    n = len(imageList)
    for i in range(n):
        imageList[i] = imageList[i].convert("RGB")

def main():
    noOfImages = int(input("Enter the number of Images that you want to convert : "))
    createImageList(noOfImages)
    convertImageList()

    element = imageList[0]
    imageList.remove(element)
    element.save("output.pdf",save_all=True,append_images=imageList)
    
imageList=[]

main()