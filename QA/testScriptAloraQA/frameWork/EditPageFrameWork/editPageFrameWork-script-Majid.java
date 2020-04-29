package com.alora.FrameworkEditPage;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class editPage {

	
	public void AccountEditPage(WebDriver driver,String FirstName, String LastName, String UserName) throws InterruptedException {
		
		
		String AccountXpath = "/html/body/div[2]/div/div/div[1]/div[2]/p[1]/a";
		driver.findElement(By.xpath(AccountXpath)).click(); 
		
		String EditAccountXpath = "/html/body/div[2]/div[1]/div/div[2]/button[1]/a"; 
		driver.findElement(By.xpath(EditAccountXpath)).click(); 
		
		
		String FirstNameID ="id_first_name";
		driver.findElement(By.id(FirstNameID)).clear();
		driver.findElement(By.id(FirstNameID)).sendKeys(FirstName);
		
		String lastNameID ="id_last_name";
		driver.findElement(By.id(lastNameID)).clear();
		driver.findElement(By.id(lastNameID)).sendKeys(LastName);
		
		String usertNameID ="id_username";
		driver.findElement(By.id(usertNameID)).clear();
		driver.findElement(By.id(usertNameID)).sendKeys(UserName);
		
		Thread.sleep(2000);
		
		//String SaveChangeBtn = "buttonstandard";    
		//driver.findElement(By.id(SaveChangeBtn)).click(); 
		
	}
}
