package com.alora.signup;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class signup {

	
	public static void main(String[] args) throws InterruptedException {
		
		
		String PATH = "C:\\Users\\java\\Desktop\\Selenium setup\\firefox Driver\\geckodriver.exe";
		System.setProperty("webdriver.gecko.driver", PATH);		
		
		WebDriver driver =  new FirefoxDriver();
		
		driver.manage().window().maximize();
		
		//step 1: Launch firefox and navigate to URL
		driver.get("http://aloradevs.ddns.net/");
		
		//step 3: Navigate to Signup page
		
		String loginXpath = "/html/body/header/div/nav/ul/li[8]/a";
		driver.findElement(By.xpath(loginXpath)).click();
		
		String signUpXpath = "/html/body/div/p[3]/a";
		driver.findElement(By.xpath(signUpXpath)).click();	
		
		String firstNameID = "id_first_name";
		driver.findElement(By.id(firstNameID)).sendKeys("majid");
		
		String lastNameID = "id_last_name";
		driver.findElement(By.id(lastNameID)).sendKeys("masood");
		
		String phoneID = "id_phone";
		driver.findElement(By.id(phoneID)).sendKeys("9735666140");
		
		String emailID = "id_email";
		driver.findElement(By.id(emailID)).sendKeys("majid_masood@bloomfield.edu");
		
		String confirmEmailID = "id_email2";
		driver.findElement(By.id(confirmEmailID)).sendKeys("majid_masood@bloomfield.edu");	
		
		String userNameID = "id_username";
		driver.findElement(By.id(userNameID)).sendKeys("majid");
		
		String passwordID = "id_password1";
		driver.findElement(By.id(passwordID)).sendKeys("Passaic6787");
		
		String confirmPasswordID = "id_password2";
		driver.findElement(By.id(confirmPasswordID)).sendKeys("Passaic6787");
		
		String btnSignUpID = "buttonstandard";
		driver.findElement(By.id(btnSignUpID)).click();
		
		Thread.sleep(5000);
		driver.quit();
		
		
		
		
		
	}
}
