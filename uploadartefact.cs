using System;
using System.IO;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        string filePath = @"C:\Users\Michi\Downloads\upload-artifact-4.6.2\example.txt";
        string uploadUrl = "https://example.com/upload";
        long maxFileSizeInBytes = 5 * 1024 * 1024; // 5 MB

        // Prüfen, ob die Datei existiert
        if (!File.Exists(filePath))
        {
            Console.WriteLine("Die Datei existiert nicht.");
            return;
        }

        // Dateigröße prüfen
        FileInfo fileInfo = new FileInfo(filePath);
        if (fileInfo.Length > maxFileSizeInBytes)
        {
            Console.WriteLine($"Die Datei ist zu groß. Maximale erlaubte Größe: {maxFileSizeInBytes / (1024 * 1024)} MB.");
            return;
        }

        // Hash der Datei berechnen
        string fileHash = CalculateFileHash(filePath);
        Console.WriteLine($"Berechneter Hash: {fileHash}");

        // Datei hochladen
        try
        {
            using (var client = new HttpClient())
            using (var content = new MultipartFormDataContent())
            using (var fileStream = new FileStream(filePath, FileMode.Open, FileAccess.Read))
            {
                content.Add(new StreamContent(fileStream), "file", Path.GetFileName(filePath));
                content.Add(new StringContent(fileHash), "fileHash"); // Hash als zusätzlichen Parameter senden

                HttpResponseMessage response = await client.PostAsync(uploadUrl, content);

                if (response.IsSuccessStatusCode)
                {
                    string responseContent = await response.Content.ReadAsStringAsync();
                    Console.WriteLine("Datei erfolgreich hochgeladen.");
                    Console.WriteLine($"Server-Antwort: {responseContent}");
                }
                else
                {
                    Console.WriteLine($"Fehler: {response.StatusCode}");
                    string errorContent = await response.Content.ReadAsStringAsync();
                    Console.WriteLine($"Fehlerdetails: {errorContent}");
                }
            }
        }
        catch (HttpRequestException ex)
        {
            Console.WriteLine($"Netzwerkfehler: {ex.Message}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ein unerwarteter Fehler ist aufgetreten: {ex.Message}");
        }
    }

    static string CalculateFileHash(string filePath)
    {
        using (var sha256 = SHA256.Create())
        using (var fileStream = new FileStream(filePath, FileMode.Open, FileAccess.Read))
        {
            byte[] hashBytes = sha256.ComputeHash(fileStream);
            return BitConverter.ToString(hashBytes).Replace("-", "").ToLowerInvariant();
        }
    }
    private void EncryptAndSaveFile(string filePath, Stream fileStream)
    {
        using (var aes = Aes.Create())
        {
            aes.Key = Encoding.UTF8.GetBytes("IhrSichererSchlüssel1234567890123456"); // 32 Byte Schlüssel
            aes.IV = Encoding.UTF8.GetBytes("InitialVector1234"); // 16 Byte IV

            using (var cryptoStream = new CryptoStream(
                new FileStream(filePath, FileMode.Create),
                aes.CreateEncryptor(),
                CryptoStreamMode.Write))
            {
                fileStream.CopyTo(cryptoStream);
            }
        }
    }
}

[ApiController]
[Route("upload")]
public class UploadController : ControllerBase
{
    [HttpPost]
    public async Task<IActionResult> UploadFile(IFormFile file, [FromForm] string fileHash)
    {
        if (file == null || file.Length == 0)
        {
            return BadRequest("Keine Datei hochgeladen.");
        }

        // Temporäre Datei speichern
        string tempFilePath = Path.GetTempFileName();
        using (var stream = new FileStream(tempFilePath, FileMode.Create))
        {
            await file.CopyToAsync(stream);
        }

        // Hash der empfangenen Datei berechnen
        string calculatedHash = CalculateFileHash(tempFilePath);

        // Hash vergleichen
        if (!string.Equals(calculatedHash, fileHash, StringComparison.OrdinalIgnoreCase))
        {
            System.IO.File.Delete(tempFilePath); // Temporäre Datei löschen
            return BadRequest("Datei ist beschädigt oder Hash stimmt nicht überein.");
        }

        // Sicherer Speicherort
        string storagePath = Path.Combine("C:\\SecureStorage", Path.GetFileName(file.FileName));

        // Datei verschlüsselt speichern
        using (var fileStream = new FileStream(tempFilePath, FileMode.Open, FileAccess.Read))
        {
            EncryptAndSaveFile(storagePath, fileStream);
        }

        // Temporäre Datei löschen
        System.IO.File.Delete(tempFilePath);

        return Ok("Datei erfolgreich hochgeladen und sicher gespeichert.");
    }

    private string CalculateFileHash(string filePath)
    {
        using (var sha256 = SHA256.Create())
        using (var fileStream = new FileStream(filePath, FileMode.Open, FileAccess.Read))
        {
            byte[] hashBytes = sha256.ComputeHash(fileStream);
            return BitConverter.ToString(hashBytes).Replace("-", "").ToLowerInvariant();
        }
    }
}
if (!File.Exists(filePath))
{
    Console.WriteLine("Die Datei existiert nicht.");
    return;
}

if (Path.GetExtension(filePath) != ".txt")
{
    Console.WriteLine("Ungültiges Dateiformat. Nur .txt-Dateien sind erlaubt.");
    return;
}
try
{
    HttpResponseMessage response = await client.PostAsync(uploadUrl, content);
    response.EnsureSuccessStatusCode(); // Löst eine Ausnahme aus, wenn der Statuscode kein Erfolg ist
}
catch (HttpRequestException ex)
{
    Console.WriteLine($"Netzwerkfehler: {ex.Message}");
}
catch (Exception ex)
{
    Console.WriteLine($"Ein unerwarteter Fehler ist aufgetreten: {ex.Message}");
}
string storagePath = Path.Combine("C:\\SecureStorage", file.FileName);
string safeFileName = Path.GetFileName(file.FileName); // Nur den Dateinamen extrahieren
string uniqueFileName = $"{Guid.NewGuid()}_{safeFileName}";
