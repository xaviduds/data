testFile = open(r"createdWithPython/test.txt", "w")
testFile.write("test2")
testFile.close()

testHTMLFile = open(r"createdWithPython/index.html", 'w')
testHTMLFile.write("<h1>Hello World!</h1>")
testHTMLFile.write("<p>paragraph</p>")
testHTMLFile.close()

testHTMLFile = open(r"createdWithPython/index.html", 'w')
testHTMLFile.write(
    "<!DOCTYPE html><html><head><title>Python-created HTML</title><h1>My first Python-generated web page!</h1></head><body><p>lorem ipsum</p></body></html>")
testHTMLFile.close()
