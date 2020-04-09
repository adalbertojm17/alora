package com.alora.home;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class userDetails {

	
	public static void main(String[] args) throws InterruptedException {
		String PATH = "C:\\Users\\java\\Desktop\\Selenium setup\\firefox Driver\\geckodriver.exe";
		System.setProperty("webdriver.gecko.driver", PATH);		
		
		WebDriver driver =  new FirefoxDriver();
		
		driver.manage().window().maximize();
		
		//step 1: Launch firefox and navigate to URL
		driver.get("http://aloradevs.ddns.net/");
		
		
		//Step 2: Login with valid user name
		
		String signInXpath = "/html/body/div/p/a";
		driver.findElement(By.xpath(signInXpath)).click();
		
		String userNameXPath = "id_username";
		
		//UserName  -- Change user name 
		String userName = "majid_masood@bloomfield.edu";
		driver.findElement(By.id(userNameXPath)).sendKeys(userName);
		//Thread.sleep(2000);
		String passwordXpath = "id_password";
		//Password  -- Change password
		String password = "Passaic6787";
		driver.findElement(By.id(passwordXpath)).sendKeys(password);
		
		String btnLoginID = "buttonstandard";
		driver.findElement(By.id(btnLoginID)).click();
		
		
		Thread.sleep(3000);
		//step 3: Click on Home button 
		String HomeXpath = "/html/body/header/div/nav/ul/li[1]/a";
		driver.findElement(By.xpath(HomeXpath)).click();
		
		//Step 4: Click on Edit changes button
		String editXapth = "/html/body/div/p/a";
		driver.findElement(By.xpath(editXapth)).click();
		
		
		//Step 5: Click on Edit Account button
		String editAccountXpath = "//*[@id=\"editbutton\"]";
		driver.findElement(By.xpath(editAccountXpath)).click();
		
		
		//step 6: Change Phone number
		String phoneNoID = "id_phone";
		driver.findElement(By.id(phoneNoID)).clear();
		//Phone number  -- Change phone number
		driver.findElement(By.id(phoneNoID)).sendKeys("+19739724300"); 

		
		
		Thread.sleep(5000);
		//Step 7: Click on SAVE button
		String btnSaveID = "buttonstandard";
		driver.findElement(By.id(btnSaveID)).click();
		
		
		
	}

}
