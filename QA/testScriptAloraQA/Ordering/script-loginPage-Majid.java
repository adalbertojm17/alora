package com.alora.orderwithoutFW;

import java.io.IOException;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class loginNotepad {

	public static void main(String[] args) throws IOException, InterruptedException{
		String PATH = "C:\\Users\\java\\Desktop\\Selenium setup\\firefox Driver\\geckodriver.exe";
		System.setProperty("webdriver.gecko.driver", PATH);		
		
		WebDriver driver =  new FirefoxDriver();
		driver.manage().window().maximize();
		
		String userName = "majidmasood";
		String passWord ="*****";
		String StoreName = "bloomfield";
		String StreetName = "davey Street";
		String APTSuite = "Suite";
		String City = "bloomfield";
		String State = "Guam";
		String zipCode = "07004";
		String datetime = "Wed Apr 17, 2020 12:05 pm";
		String StreetNameDP = "Bay Street1";
		String APTSuiteDP = "APT";
		String CityDP = "MM";
		String StateDP = "Guam";
		String zipCodeDP = "07004";
		String datetimeDP = "Wed Apr 18, 2020 12:05 pm";
		
		loginNotepad ln = new loginNotepad();
		
		ln.login(userName,passWord,driver);
		
		Orderplacement1 op = new Orderplacement1();
		
		op.orderplacement1(driver,StoreName,StreetName,APTSuite,City,State,zipCode,datetime,StreetNameDP,
				APTSuiteDP,CityDP,StateDP,zipCodeDP,datetimeDP);
		
	}
	
	public void login(String ipuserName,String ippassWord, WebDriver driver) throws InterruptedException {
		
		//step 1: Launch firefox and navigate to URL
		driver.get("https://aloradevs.ddns.net/");
		
		//step 2: Click on Login button
		String login_Xpath = "/html/body/header/div/nav/ul/li[4]/a";
		driver.findElement(By.xpath(login_Xpath)).click(); 
		
		//Step 3: Enter Username and password
		Thread.sleep(5000);
		
		String userNameXPath = "id_username";
		String userName = ipuserName;
		driver.findElement(By.id(userNameXPath)).sendKeys(userName);
		//Thread.sleep(2000);
		String passwordXpath = "id_password";
		String password = ippassWord;
		driver.findElement(By.id(passwordXpath)).sendKeys(password);
		
		
		//Step 4: Click on Login Button
		
		String loginBtn = "buttonstandard";
		driver.findElement(By.id(loginBtn)).click();
		
		Thread.sleep(2000);
	
	}

}
