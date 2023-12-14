# Cloud Time GDSC Udinus


*Demo 1 - Simple Quiz Website App with Cloud Run and Vertex AI*

1. Pada quiz-generator/main.py line 46:
    -> Jangan lupa memasukkan project id masing-masing pada tempat yang disediakan

        Contoh:
        misal mempunyai project dengan id "my-project-id-234", maka:

        vertexai.init(project="<YOUR PROJECT ID>", location="us-central1")  #<-CHANGED

        menjadi:

        vertexai.init(project="my-project-id-234", location="us-central1")  #<-CHANGED

2. Proses lainnya sesuai dengan yang ada di video