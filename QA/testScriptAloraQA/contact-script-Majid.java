package com.alora.contactus;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class contactUs {

	public static void main(String[] args) throws InterruptedException {
		String PATH = "C:\\Users\\java\\Desktop\\Selenium setup\\firefox Driver\\geckodriver.exe";
		System.setProperty("webdriver.gecko.driver", PATH);		
		
		WebDriver driver =  new FirefoxDriver();
		
		driver.manage().window().maximize();
		
		//step 1: Launch firefox and navigate to URL
		driver.get("http://aloradevs.ddns.net/");
		
		Thread.sleep(3000);
		//step 2: Click on Contact Us 
		
		String contactUSXpath = "/html/body/header/div/nav/ul/li[7]/a";
		driver.findElement(By.xpath(contactUSXpath)).click();
		
		//step 3: Click on FirstName

		String inputFirstNameID = "id_first_name";
		driver.findElement(By.id(inputFirstNameID)).sendKeys("majid"); 
		
		String inputLastNameID = "id_last_name";
		driver.findElement(By.id(inputLastNameID)).sendKeys("masood");
		
		String inutEmailID = "id_email";
		driver.findElement(By.id(inutEmailID)).sendKeys("majid_masood@bloomfield.edu");
		
		String inputServicesID = "id_services";
		driver.findElement(By.id(inputServicesID)).sendKeys("Dry Cleaning");
		
		String inputContentID = "id_content";
		driver.findElement(By.id(inputContentID)).sendKeys("Test");
		
		
		Thread.sleep(5000);
		
		String btnSubmitID = "buttonstandard";
		driver.findElement(By.id(btnSubmitID)).click();
		
		
		
		
		
				
				
		
		
		
		


	}

}
