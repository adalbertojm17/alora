package com.alora.services;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class servicesTab {

	
	public static void main(String[] args) throws InterruptedException {
		String PATH = "C:\\Users\\java\\Desktop\\Selenium setup\\firefox Driver\\geckodriver.exe";
		System.setProperty("webdriver.gecko.driver", PATH);		
		
		WebDriver driver =  new FirefoxDriver();
		
		driver.manage().window().maximize();
		
		//step 1: Launch firefox and navigate to URL
		driver.get("https://aloradevs.ddns.net/");
		
		//step 2: Click on Login button
		String login_Xpath = "/html/body/header/div/nav/ul/li[4]/a";
		driver.findElement(By.xpath(login_Xpath)).click(); 
		
		//Step 3: Enter Username and password
		Thread.sleep(5000);
		
		String userNameXPath = "id_username";
		String userName = "majida5";
		driver.findElement(By.id(userNameXPath)).sendKeys(userName);
		//Thread.sleep(2000);
		String passwordXpath = "id_password";
		String password = "David@123";
		driver.findElement(By.id(passwordXpath)).sendKeys(password);
		
		
		//Step 4: Click on Login Button
		
		String loginBtn = "buttonstandard";    
		driver.findElement(By.id(loginBtn)).click();
		
		Thread.sleep(2000);
		
		String serviceXpath = "/html/body/header/div/nav/ul/li[5]/a";
		driver.findElement(By.xpath(serviceXpath)).click();
		
		String companyXpath = "//*[@id=\"company\"]";
		driver.findElement(By.xpath(companyXpath)).sendKeys("Laundry");
		
		String searchBtn = "buttonstandard";    
		driver.findElement(By.id(searchBtn)).click();
		
		String companyOutputXpath = "/html/body/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td";
		String companyValue = driver.findElement(By.xpath(companyOutputXpath)).getText();
		
		System.out.println(companyValue);
		
		
		
		
		
		
		
	}
}
