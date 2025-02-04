package ejercicios;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class Ejercicio1 {
	
	static WebDriver driver1;
	static String url = "http://localhost:3000/";
	
	@BeforeAll
	static void setURL() {
		driver1 = new ChromeDriver();
	}

	@Test
	void testCabecera() {
		driver1.get(url);
		WebElement cabecera = driver1.findElement(By.id("Cabecera"));
		
		String texto = cabecera.getText();
		assertEquals("Enlaces Favoritos", texto);
	}
	
	@Test
	void testLista() {
		driver1.get(url);
		WebElement cabecera = driver1.findElement(By.id("ListaEnlaces"));
		
		String texto = cabecera.getText();
		assertEquals("Enlaces Favoritos", texto);
	}

}
