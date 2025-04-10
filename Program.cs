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

        using (var client = new HttpClient())
        using (var content = new MultipartFormDataContent())
        using (var fileStream = new FileStream(filePath, FileMode.Open, FileAccess.Read))
        {
            content.Add(new StreamContent(fileStream), "file", Path.GetFileName(filePath));
            HttpResponseMessage response = await client.PostAsync(uploadUrl, content);

            if (response.IsSuccessStatusCode)
            {
                Console.WriteLine("Datei erfolgreich hochgeladen.");
            }
            else
            {
                Console.WriteLine($"Fehler: {response.StatusCode}");
            }
        }
    }
}
