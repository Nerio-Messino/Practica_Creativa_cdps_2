import subprocess 

#Nos situamos en el directorio correspondiente y ejecutamos el comando que nos piden para ajustar las versiones

subprocess.call[("src/reviews")]
subprocess.call[("docker run --rm -u root -v $(pwd):/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build")]