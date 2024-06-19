import os
from pypdf import PdfReader

path = "data"
os.makedirs(path)

for file in os.listdir("reference"):
    file = file
    reader = PdfReader("reference" + "/" + file)
    cnt = 0
    new_path = "data/" + file[:-4]
    os.makedirs(new_path)
    for page in reader.pages:
        text = page.extract_text()
        cnt += 1
        with open(new_path + "/" + file[:-4] + "_" + str(cnt) + ".txt", "a") as f:
            f.write(text)
            f.close()