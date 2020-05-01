package com.alora.tracking;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

public class tracking {

	public static void main(String[] args) throws InterruptedException {
		String PATH = "C:\\Users\\java\\Desktop\\Selenium setup\\firefox Driver\\geckodriver.exe";
		System.setProperty("webdriver.gecko.driver", PATH);		
		
		WebDriver driver =  new FirefoxDriver();
		
		driver.manage().window().maximize();
		
		//step 1: Launch firefox and navigate to URL
		//driver.get("https://aloradevs.ddns.net/");
		driver.get("https://aloraqa.ddns.net/");
		
		//step 2: Click on Login button
		String login_Xpath = "/html/body/header/div/nav/ul/li[4]/a";
		driver.findElement(By.xpath(login_Xpath)).click(); 
		
		//Step 3: Enter Username and password
		Thread.sleep(5000);
		
		String userNameXPath = "id_username";
		String userName = "majidd";
		driver.findElement(By.id(userNameXPath)).sendKeys(userName);
		//Thread.sleep(2000);
		String passwordXpath = "id_password";
		String password = "David@1234";
		driver.findElement(By.id(passwordXpath)).sendKeys(password);
		
		
		//Step 4: Click on Login Button
		
		String loginBtn = "buttonstandard";    
		driver.findElement(By.id(loginBtn)).click();
		
		Thread.sleep(2000);
		
		
		String trackingXpath = "/html/body/header/div/nav/ul/li[4]/a";
		driver.findElement(By.xpath(trackingXpath)).click(); 
	
		
		String trackingID ="id_q";
		driver.findElement(By.id(trackingID)).clear();
		driver.findElement(By.id(trackingID)).sendKeys("1");
		
		String trackXpath ="//*[@id=\"=\"]";
		driver.findElement(By.xpath(trackXpath)).click();
	
		
		Thread.sleep(2000);
		
		String iconXPath = "/html/body/div[2]/div/div[2]/div/div[1]/div";
		boolean trackStatus = driver.findElement(By.xpath(iconXPath)).isEnabled();
		
		if(trackStatus = true)
		{
			System.out.println("PASS");
		}else
		{
			System.out.println("FAIL");
		}
		 
		
		
		
		

	}
}
