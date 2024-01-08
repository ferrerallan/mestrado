const axios = require('axios');

let config = {
  method: 'get',
  maxBodyLength: Infinity,
  url: 'https://browser.ihtsdotools.org/fhir/CodeSystem/$lookup?system=http://snomed.info/sct&code=427623005&property=normalForm&property=sufficientlyDefined\n',
  headers: { }
};

axios.request(config)
.then((response) => {
  console.log(JSON.stringify(response.data));
})
.catch((error) => {
  console.log(error);
});
