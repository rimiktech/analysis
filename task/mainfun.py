from time import sleep

print("my name is najmus ")

def process_data(data):
    print("begining the data processing...")
    modified_data = data + " that has been modified"
    sleep(3)
    print("Data processing finisher.")
    return modified_data

def main():
    data= "my data read the web"
    print(data)
     
    modified_data= process_data(data)
    print(modified_data)

if __name__ == "__main__":
    data = "My data read from the Web"
    print(data)
    modified_data = process_data(data)
    print(modified_data)



