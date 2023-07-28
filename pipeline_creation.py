import http.client
import json

conn = http.client.HTTPSConnection("codedev.ms")

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic Om5ia2V0cXlwZWRqYjNhaTZoemp5ZmM2cmtodWRkeWl6eGNod213djZwanMzYmNrcnVndHE=',
  'Cookie': 'VstsSession=%7B%22PersistentSessionId%22%3A%225a50ea01-0f64-4f0f-89e9-cdc8c1f7aefc%22%2C%22PendingAuthenticationSessionId%22%3A%2200000000-0000-0000-0000-000000000000%22%2C%22CurrentAuthenticationSessionId%22%3A%2200000000-0000-0000-0000-000000000000%22%2C%22SignInState%22%3A%7B%7D%7D'
}

i = 1
while i < 200:
    path = "pipeline_" + str(i) + "/pipeline_" + str(i) + ".yml"
    name = "pipeline_" + str(i)
    d = {
      "configuration": {
        "repository": {
          "fullName": "andreaschelsau/definitions",
          "connection": {
            "id": "b8329b70-ab37-40ac-a9b1-9fb2bceb9609"
          },
          "type": "gitHub"
        },
        "type": "yaml"
      },
      "folder": "pipelineFromAPIFolder4"
    }
    d["configuration"]["path"] = path
    d["name"] = name
    payload = json.dumps(d)
    print(path)
    print(name)
    conn.request("POST", "/achelsau-dev/MyFirstProject/_apis/pipelines?api-version=7.0", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    i += 1