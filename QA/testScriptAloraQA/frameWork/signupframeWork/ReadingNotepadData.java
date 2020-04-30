package com.alora.FrameWorkOrder;


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
		
		String TestFile = "C:\\Users\\java\\Desktop\\Framework\\OrderDataNotepad.txt";
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
			String StreetName = parameter[3];
			String APTSuite = parameter[4];
			String City = parameter[5];
			String State = parameter[6];
			String zipCode = parameter[7];
			String datetime = parameter[8];
			String StreetNameDP = parameter[9];
			String APTSuiteDP = parameter[10];
			String CityDP = parameter[11];
			String StateDP = parameter[12];
			String zipCodeDP = parameter[13];
			String datetimeDP = parameter[14];
			
			
			loginNotepad	ss = new loginNotepad();
			
			ss.login(userName, passWord, driver);
 
			Orderplacement op = new Orderplacement();
			
			op.orderplacement1(driver,StoreName,StreetName,APTSuite,City,State,zipCode,datetime,StreetNameDP,
					APTSuiteDP,CityDP,StateDP,zipCodeDP,datetimeDP);
			
		}
	}
}
