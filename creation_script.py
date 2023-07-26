import os
import time

# checking if the directory demo_folder 
# exist or not.
path = "D:\\test_projects\\definitions\\"
yml_content = "pool:\r\n" + "  name: Default\r\n" + "  vmImage: windows-latest\r\n" + "\r\n" + "steps:\r\n" + "- script: echo Hello, world!\r\n" + "  displayName: 'Run a one-line script'\r\n"

for i in range(200):
	new_path = path + "pipeline_" + str(i)
	print(new_path)
	if not os.path.exists(new_path):
		os.makedirs(new_path)
	#time.sleep(0.5)
	f = open(new_path + "\\pipeline_" + str(i) + ".yml", "a")
	f.write(yml_content)
	f.close()
