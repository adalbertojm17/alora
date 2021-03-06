package com.alora.FrameworkContact;


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
		
		String TestFile = "C:\\Users\\java\\Desktop\\Framework\\ContactUs.txt";
		FileReader FR = new FileReader(TestFile);
		BufferedReader BR = new BufferedReader(FR);
		String parameters = "";
		BR.readLine();		
				
		//Loop to read all lines one by one from file and print It.
		while((parameters = BR.readLine())!= null) {
			String[] parameter = parameters.split("\\|");
			String userName = parameter[0];
			String passWord = parameter[1];
			String StoreName = parameter[2];
			String Subject = parameter[3];
			String Content = parameter[4];
						
			
			loginNotepad	ss = new loginNotepad();
			
			ss.login(userName, passWord, driver);
 
			ContactUs us  = new ContactUs();
			
			us.fmContactUs(driver,StoreName,Subject,Content);
			
		}
	}
}
