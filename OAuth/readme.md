Men Robotmanmi ?

Internet -- jang maydoni. Bir qarashda xavfsizdek ko'ringan internet-magazin, moshenniklaniki bo'lib
chiqishi mumkin. E-mail ga kelgan oddiy xat, fishing bo'lib chiqishi mumkin. Qiziqarli reklama
sizni virusi bor saytga kiritib qo'yishi mumkin. Sizni kompyuteringiz va data larinigizni eng
zo'r himoyalash yo'li,bu -- kompyuterni internetdan o'chirish va uni seyfga qulflab qo'yish. 😄 hazil albatta !

Gap orasida, hakerlar hujumiga, e'tiborsiz bo'lgan userlar emas, balki barcha xavfsizlikni shartlarini
qilgan eng zo'r user ham uchrashi mumkin. Oddiygina ilovani internetga yuklashni olsak. Shuning uchun
har doim, o'z qilayotgan ishimizni haker nazari bilan ham qarab ko'rishimiz kerak.

Internetda har xil yomon botlar aylanib yuribdi: qidiruv o'rgimchaklari yoki parser, cheker.
Ulardan ko'pi, o'zini xuddi yaxshi botdek ko'rsatadi. Internetdagi saytlar haqida ma'lumot yig'adi
ba'zi birlari esa o'zini agressiv tutadi. ochiq forumlarni spamga to'ldiradi, har xil XSS hujumlar qiladi, 
ko'plab yoq userlarni ro'yxatdan o'tkazadi. 

Aynan shuning uchun ham saytlarda Captcha degan narsa bor. Bu saytlarni parserdan va hakerlarni ma'lumotlarni yig'ishidan asraydi. 

CAPTCHA ( Completely Automated Public Turing test to tell Computers and Humans Apart ) - odamlar va kompyuterlarni farqlaydigan, to'liq avtomatizatsiya qilingan ommaviy Tyuring testi. 1990-93 yillarda keng foydalanish boshlangan. 2014 yilda esa Google o'zini reCaptcha sini chiqargandan keyin, aynan shu versiya ommalashib ketgan. Aynan hozir, siz-u biz ko'radigan reCaptcha, Google tomonidan tayyorlangan.



Bundan tashqari yana 2 faktorli kirish ham bor. Bu sms orqali kod olish. SMS kodni buzish uchun, o'sha telefonga access va SS7 kerak. va vualya, sms kodni olib, hujum qilish mumkin. 

SMS kod olish alternativasi va Eng kuchli himoya esa -- TOTP orqali ilova (app) ichida kod kelishi,  ya'ni Time-Based One-Time Password Algorithm.
(-- auth.py faylida yozib chiqdik. )
Eng mashhurlari esa Google Authenticator va Authy.


TOTP kod orqali userni verifikatsiya qilish algoritmi:

-- user uchun secret code generit qilish
-- shu secret code asosida provisioning-havola generit qilish, ( bu generit, kodni mobile ga yuborish uchun )
--
