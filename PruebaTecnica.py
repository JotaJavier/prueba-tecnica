from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.add_argument("start-maximized")
options.add_argument('--disable-extensions')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

wait = WebDriverWait(driver, 20)

#usuario
username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
username_field.send_keys("Admin")

# contrasena
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("admin123") 

# clic en el botón de inicio de sesión
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()


# Esperar a que se cargue el dashboard (espera hasta que el Dashboard esté visible)
dashboard_element = wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

# clic en la pestaña Recruitment
recruitment_tab = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Recruitment']")))
recruitment_tab.click()

# click en el boton add
add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Add ']")))
add_button.click()

#PRIMARA VENTANA

# Rellenar el campo First Name
first_name = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
first_name.send_keys("nelson")

# Rellenar el campo Middle Name
middle_name = driver.find_element(By.NAME, "middleName")
middle_name.send_keys("manuel")

# Rellenar el campo Last Name
last_name = driver.find_element(By.NAME, "lastName")
last_name.send_keys("Doria")

# Seleccionar una vacante en el campo Vacancy
vacancy_dropdown = driver.find_element(By.XPATH, "//label[text()='Vacancy']/following::div[@class='oxd-select-text-input']")
vacancy_dropdown.click()

vacancy_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='test']")))
vacancy_option.click()

# Rellenar el campo Email
email_field = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/input")))
email_field.send_keys("jesus.javier@mail.com")

# Rellenar el campo Contact Number
contact_field = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/input")))
contact_field.send_keys("1234567890")

# Subir un archivo
resume_upload = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
resume_upload.send_keys("C:/Reto Técnico Analista pruebas generalista con automatización.pdf")

keywords_field = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[5]/div/div[1]/div/div[2]/input")))
keywords_field.send_keys("Python, Selenium, pruebas")

notes_field = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[6]/div/div/div/div[2]/textarea")))
notes_field.send_keys("Esta es una prueba")

consent_checkbox = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[7]/div/div/div/div[2]/div/label/span")))
consent_checkbox.click()

save_button = driver.find_element(By.XPATH, "//button[text()=' Save ']")
save_button.click()

#SEGUNDA VENTANA
shorlist_button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div[1]/form/div[2]/div[2]/button[2]")))
shorlist_button.click()

#TERCERA VENTANA
notes_field_2 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/textarea")))
notes_field_2.send_keys("shorlist candidate")

save_button_2 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]")))
save_button_2.click()

#CUARTA VENTANA
shedule_interview_button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div[1]/form/div[2]/div[2]/button[2]")))
shedule_interview_button.click()

#QUINTA VENTANA
interviewer_field = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div/div[2]/div/div/input")))
interviewer_field.send_keys("Amelia")
interviewer_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Amelia  Brown']")))
interviewer_field.click()

date_field = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[3]/div/div[2]/div/div/input")))
date_field.send_keys('2024-16-09')

hour_field = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div/input")))
hour_field.click()

notes_field_3 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/textarea")))
notes_field_3.send_keys("Schedule Interview")

interwiew_field = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input"))
)
interwiew_field.send_keys("interwiew Tittle")

save_button_3 = driver.find_element(By.XPATH, "//button[text()=' Save ']")
save_button_3.click()


#SEXTA VENTANA
mark_interwiew_passed_button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div[1]/form/div[2]/div[2]/button[3]")))
mark_interwiew_passed_button.click()

#SEPTIMA VENTANA
notes_field_4 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/textarea")))
notes_field_4.send_keys("Mark Interview Passed")

save_button_4 = driver.find_element(By.XPATH, "//button[text()=' Save ']")
save_button_4.click()

#OCTAVA VENTANA
offer_job_button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div[1]/form/div[2]/div[2]/button[3]")))
offer_job_button.click()

#NOVENA VENTANA
notes_field_5 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/textarea")))
notes_field_5.send_keys("Offer Job")

save_button_5 = driver.find_element(By.XPATH, "//button[text()=' Save ']")
save_button_5.click()

#DECIMA VENTANA
hire_button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div[1]/form/div[2]/div[2]/button[3]")))
hire_button.click()

#UNDECIMA VENTANA
notes_field_6 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/textarea")))
notes_field_6.send_keys("Hire Candidate")

save_button_6 = driver.find_element(By.XPATH, "//button[text()=' Save ']")
save_button_6.click()

#REDIRECCION A VENTANA RECRUITMENT
recruitment_tab = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Recruitment']")))
recruitment_tab.click()


input("Presiona Enter para cerrar el navegador...")
driver.quit()  # Cerrará el navegador después de presionar Enter