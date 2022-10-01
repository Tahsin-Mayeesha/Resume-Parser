from pyresparser import ResumeParser
data = ResumeParser('tahsin_mayeesha.pdf').get_extracted_data()
print(data)