import os
  
# checking if the directory demo_folder 
# exist or not.
path = 'D:\test_projects\definitions\'
yml_content = "pool:
  name: Default
  vmImage: windows-latest
  
steps:
- script: echo Hello, world!
  displayName: 'Run a one-line script'"
for i in range(200):
	new_path = path + "pipeline_" + i
	if not os.path.exists(new_path):
		os.makedirs(new_path)
	f = open(new_path + "\pipeline_" + i + ".yml", "a")
	f.write(yml_content)
	f.close()
		
