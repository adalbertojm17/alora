package com.alora.FrameworkContact;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class ContactUs {

	
	public void fmContactUs(WebDriver driver,String storevalue,String subject, String content) {
		
		//Step 1: Click on Main button
		String contactUsXpath = "/html/body/header/div/nav/ul/li[7]/a";
		driver.findElement(By.xpath(contactUsXpath)).click(); 
		
		//Step 2: Click onOrder Placement
		String storeID = "id_store";
		driver.findElement(By.id(storeID)).sendKeys(storevalue);
		
		String subjectID = "id_subject";
		driver.findElement(By.id(subjectID)).sendKeys(subject);
		
		String contentID ="id_content";
		driver.findElement(By.id(contentID)).sendKeys(content);
		
		String submitnBtn = "buttonstandard";
		driver.findElement(By.id(submitnBtn)).click();
		
		
	}
}
