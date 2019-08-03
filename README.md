# IPFS Gateway Tester
IPFS gateway tester runs some bare bones Python code to test the performance of common IPFS gateways. It current tests the following gateway providers:

- Protocol Labs (https://ipfs.io/ipfs/)
- Cloudflare (https://cloudflare-ipfs.com/ipfs/)
- Infura (https://ipfs.infura.io/ipfs/)
- Pinata (https://gateway.pinata.cloud/ipfs/)
- Eternum (https://ipfs.eternum.io/ipfs/)
- Siderus (https://siderus.io/ipfs/)
- Temporal (https://gateway.temporal.cloud/ipfs/)

It tests each gateway provider against three different file types:

- [Text File](https://cloudflare-ipfs.com/ipfs/QmSQfLsPDKaFJM3SPKZYU971XSCArXKVCAWcEzQaKgtxQp) (QmSQfLsPDKaFJM3SPKZYU971XSCArXKVCAWcEzQaKgtxQp)
- [Image File](https://cloudflare-ipfs.com/ipfs/QmUTcaZg3UVqKxM8GvjEVjtNaFDCsG3EAQAU4nzmdi7Vis) (QmUTcaZg3UVqKxM8GvjEVjtNaFDCsG3EAQAU4nzmdi7Vis)
- [Video File](https://cloudflare-ipfs.com/ipfs/QmbvdTQ5eCS7MqBfqv93Pdhy74p95XHuLh5nzSmaQiu6wk) (QmbvdTQ5eCS7MqBfqv93Pdhy74p95XHuLh5nzSmaQiu6wk)

# Requirements
IPFS gateway tester requires:

- Python 3.6+
- [Requests](https://2.python-requests.org/en/master/)

# Running The Test
Assuming you have Python 3.6+ installed on your computer, you can do the following:

```
git clone https://github.com/lyttlerock/ipfs-gateway-tester.git
cd ipfs-gateway-tester
virtualenv venv
pip install requests
python main.py
```
This will start the test and spit out a CSV file (results.csv) that has three columns of data:

- Provider (ex. Protocol Labs, Cloudflare, etc.
- Hash (hash of the file fetched)
- Time (in milliseconds)

You can use the hash map provided in the intro section above to make them human readable if needed.

# results/
The results directory is the output of the tests that I ran using this code. It contains results from different AWS t2.micro instances spread across geographies. Feel free to use this data if you'd like to skip running the code yourself.
