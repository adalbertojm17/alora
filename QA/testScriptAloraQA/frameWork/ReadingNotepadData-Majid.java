package com.alora.frameworkSignup;


import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class ReadingNotepadData {

	public static void main(String[] args) throws IOException, InterruptedException {
		String PATH = "C:\\Users\\java\\Desktop\\Selenium setup\\firefox Driver\\geckodriver.exe";
		System.setProperty("webdriver.gecko.driver", PATH);		
		
		WebDriver driver =  new FirefoxDriver();
		
		driver.manage().window().maximize();
		
		String TestFile = "C:\\Users\\java\\Desktop\\Framework\\FrameWorksignup\\SignUpDataNotepad.txt";
		FileReader FR = new FileReader(TestFile);
		BufferedReader BR = new BufferedReader(FR);
		String parameters = "";
		BR.readLine();		
				
		//Loop to read all lines one by one from file and print It.
		while((parameters = BR.readLine())!= null) {
			String[] parameter = parameters.split("\\|");
			String FirstName = parameter[0];
			String LastName = parameter[1];
			String PhoneNumber = parameter[2];
			String Email = parameter[3];
			String UserName = parameter[4];
			String Password = parameter[5];
			String StreetName = parameter[6];
			String APTSuite = parameter[7];
			String City = parameter[8];
			String State = parameter[9];
			String zipCode = parameter[10];
			
			
			
			signup	ss = new signup();
			
			ss.userSignUp(driver,FirstName,LastName,PhoneNumber,Email,UserName,Password,
					StreetName,APTSuite,City,State,zipCode);
 
		
		}
	}
}
