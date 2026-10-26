resources = [
[101, "Laptop", "Electronics", 8],
[102, "Projector", "Electronics", 0],
[103, "Whiteboard", "Classroom", 5],
[104, "Microphone", "Audio", 3],
[105, "Camera", "Electronics", 2]
]

def displayResources(resources):
    for x in resources:
        print(x)



def searchByCategory(resources,category):
    found=False
    for x in resources:
        if x[2]==category:
            print(x)
            found=True
    if not found:
        print('Not Found')



def findUnavailable(resources):
    unavaialbe=False
    for x in resources:
        if x[3]==0:
            print(x)
            unavaialbe=True
    if not unavaialbe:
        print('All items are available')

displayResources(resources)
searchByCategory(resources,'Audo')
findUnavailable(resources)