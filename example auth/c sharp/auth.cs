using System;
using System.Net.Http;
using System.Threading.Tasks;

namespace licensesystemauthtest
{
    class MainClass
    {
        public static async Task Main(string[] args)
        {
            string licensekey = "lkey";
            string id = "id";

            var httpClient = HttpClientFactory.Create();

            var url = "http://127.0.0.1:5000/" + licensekey + "/" + id;
            var data = await httpClient.GetStringAsync(url);

            if (data == "false")
            {
                Console.WriteLine("access denied");
            }
            else if (data == "true")
            {
                Console.WriteLine("access granted");
            }
        }
    }
}