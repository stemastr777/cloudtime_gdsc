Cloud Time GDSC Udinus


Demo 1 - Simple Quiz Website App with Cloud Run and Vertex AI

1. Pada quiz-generator/main.py line 46:
    -> Jangan lupa mengganti "<YOUR PROJECT ID>" dengan project id masing-masing

        Contoh:
        misal mempunyai project dengan id "my-project-id-234", maka:

        vertexai.init(project="<YOUR PROJECT ID>", location="us-central1")  #<-CHANGED

        berubah menjadi:

        vertexai.init(project="my-project-id-234", location="us-central1")  #<-CHANGED

2. Proses lainnya sesuai dengan yang ada di video