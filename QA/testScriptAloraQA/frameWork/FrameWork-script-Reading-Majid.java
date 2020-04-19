package FrameworkNotepad;


import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class ReadingNotepadData {

	public static void main(String[] args) throws IOException, InterruptedException {
	
		String TestFile = "C:\\Users\\java\\Desktop\\Framework\\TestDataNotepad.txt";
		FileReader FR = new FileReader(TestFile);
		BufferedReader BR = new BufferedReader(FR);
		String parameters = "";
		BR.readLine();		
				
		//Loop to read all lines one by one from file and print It.
		while((parameters = BR.readLine())!= null) {
			String[] parameter = parameters.split("\\|");
			String userName = parameter[0];
			String passWord = parameter[1];
			
			loginNotepad	ss = new loginNotepad();
			
			ss.login(userName, passWord);

		}
	}
}
