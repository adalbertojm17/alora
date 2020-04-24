package com.alora.frameworkSignup;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class signup {

	
	public void userSignUp(WebDriver driver,String FirstName,String LastName, String PhoneNumber,String Email,String UserName,String Password,
			String StreetName,String APTSuite,String City,String State,String zipCode) throws InterruptedException {
			
	//	String PATH = "C:\\Users\\java\\Desktop\\Selenium setup\\firefox Driver\\geckodriver.exe";
	//	System.setProperty("webdriver.gecko.driver", PATH);		
		
	//	WebDriver driver =  new FirefoxDriver();
		
	//	driver.manage().window().maximize();
		
		//step 1: Launch firefox and navigate to URL
		//driver.get("http://aloradevs.ddns.net/");
		driver.get("https://aloraqa.ddns.net/");
		
		
		//step 3: Navigate to Signup page
		
		String signUpXpath = "/html/body/div[2]/div/p/a";
		driver.findElement(By.xpath(signUpXpath)).click();	
		
		String loginXpath = "/html/body/div[2]/div/p[2]/a";
		driver.findElement(By.xpath(loginXpath)).click();	
		
		String firstNameID = "id_0-first_name";
		driver.findElement(By.id(firstNameID)).sendKeys(FirstName);
		
		String lastNameID = "id_0-last_name";
		driver.findElement(By.id(lastNameID)).sendKeys(LastName);
	
		String phoneID = "id_0-phone";
		driver.findElement(By.id(phoneID)).sendKeys(PhoneNumber);
		
		String emailID = "id_0-email";
		driver.findElement(By.id(emailID)).sendKeys(Email);
		
		String confirmEmailID = "id_0-email2";
		driver.findElement(By.id(confirmEmailID)).sendKeys(Email);	
		
		String userNameID = "id_0-username";
		driver.findElement(By.id(userNameID)).sendKeys(UserName);
		
		String passwordID = "id_0-password1";
		driver.findElement(By.id(passwordID)).sendKeys(Password);
		
		String confirmPasswordID = "id_0-password2";
		driver.findElement(By.id(confirmPasswordID)).sendKeys(Password);
		
		String btnSignUpID = "buttonstandard";
		driver.findElement(By.id(btnSignUpID)).click();
		
		//Step 5: Enter Street Name
		String streetXpath = "id_1-street";
		driver.findElement(By.id(streetXpath)).sendKeys(StreetName);
		
		//Step 6: Enter APT/Suite
		String APTSuiteXpath = "id_1-apt";
		driver.findElement(By.id(APTSuiteXpath)).sendKeys(APTSuite);
		
		//Step 7: Enter City 
		String cityuXpath = "id_1-city";
		driver.findElement(By.id(cityuXpath)).sendKeys(City);
		
		//Step 8: Enter State
		String stateXpath = "id_1-state";
		driver.findElement(By.id(stateXpath)).sendKeys(State);
		
		//Step 9: Enter ZipCode
		String zipCodeXpath = "id_1-zip_code";
		driver.findElement(By.id(zipCodeXpath)).sendKeys(zipCode);
		
		Thread.sleep(5000);
		
		String contuinueXpath="//*[@id=\"buttonstandard\"][2]";
		driver.findElement(By.xpath(contuinueXpath)).click();
		
		
		Thread.sleep(5000);
		//driver.quit();
		
		
		
		
		
	}
}
