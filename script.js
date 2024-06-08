//-----------------------------READ--------------------------------

async function read() {
  const form = document.getElementById("fileUploadForm");
  const formData = new FormData(form);

  try {
    const request = await fetch("http://localhost:5173/upload", {
      method: "POST",
      body: formData,
    });
    const message = await request.text();
    console.log(message);

    //getting the column names
    const optionResponse = await fetch("http://localhost:5173/getColumns");
    let options = await optionResponse.text();
    options = options.split(/\r?\n/).filter((value) => value.trim() !== "");

    //inserting the select box
    const extractAttributeContainer = document.getElementById(
      "extractAttributeContainer"
    );
    extractAttributeContainer.innerHTML = `<h2 style="padding-top:15px;">Select the attribute: </h2>`;
    const extractAttributeSelect = document.createElement("select");
    extractAttributeSelect.setAttribute("id", "extractAttribute");
    extractAttributeSelect.setAttribute("style", `margin: 10px`);
    // extractAttributeSelect.setAttribute("onchange", `getData()`);
    extractAttributeContainer.appendChild(extractAttributeSelect);

    for (let i = 0; i < options.length; i++) {
      const option = document.createElement("option");
      option.setAttribute("value", `${option[i + 1]}`);
      option.innerHTML = options[i];
      extractAttributeSelect.appendChild(option);
    }

    const allElementsOption = document.createElement("option");
    allElementsOption.setAttribute("value", `${options[options.length]}`);
    allElementsOption.innerHTML = `All Attributes`;
    extractAttributeSelect.appendChild(allElementsOption);

    //button
    const extractButton = document.createElement("button");
    extractButton.setAttribute(
      "class",
      `transition ease-in-out cursor-pointer bg-blue-900 hover:-translate-y-1 hover:scale-110 hover:bg-purple-900 duration-300 text-white font-bold rounded-md`
    );
    extractButton.setAttribute(
      "style",
      `padding:16px 40px;`
    );
    extractButton.setAttribute("type", `button`);
    extractButton.setAttribute("id", "extractButton");
    extractButton.setAttribute("onclick", "getData()");
    extractButton.innerHTML = `Extract`;
    extractAttributeContainer.appendChild(extractButton);

    //add content to graph section
    const selectGraph = document.getElementById("selectGraph");
    selectGraph.innerHTML = `<div>
      <form style="display:flex; justify-content:center;" id="graphSelect">
        <div style = "margin-top: 12px; display:flex; justify-content: center">
          <div style = "margin-top:10px;">
            <label for="graphOptions">Select the type of graph:</label>
            <select
              id="graphOptions"
              name="graphOptions"
              onchange="selectGraph()"
            >
                <option value="option1">Histogram</option>
                <option value="option2">Box Plot</option>
                <option value="option3">Pie Chart</option>
                <option value="option4">Line Graph</option>
                <option value="option5">Bar Graph</option>
                <option value="option6">Scatter Plot</option>
                <option value="option7">Contour Plot</option>
                <option value="option8">Heat Map</option>
            </select>
          </div>
          <div id="attributeContainer"></div>
        </div>
        <div>
          <button style = "padding:16px 40px; margin: 7px 0px -29px 13px" 
                  class = "transition ease-in-out cursor-pointer bg-blue-900 hover:-translate-y-1 hover:scale-110 hover:bg-purple-900 duration-300 text-white font-bold rounded-md" 
                  type="button" 
                  id="generateButton"
                  onclick="generateGraph()">
            Generate
          </button>
        </div>
      </form>
    
    </div>`;

    //getting options for the graph
    const attributeContainer = document.getElementById("attributeContainer");
    document.getElementById("defaultMessage").innerHTML = "";

    const attributeSelectX = document.createElement("select");
    attributeSelectX.setAttribute("id", "attributeSelectX");
    attributeSelectX.setAttribute("style", `margin: 10px`);

    attributeContainer.appendChild(attributeSelectX);

    for (let i = 0; i < options.length; i++) {
      const option = document.createElement("option");
      option.setAttribute("value", `${options[i]}`);
      option.innerHTML = options[i];
      attributeSelectX.appendChild(option);
    }

    const fileInput = document.getElementById("fileInput");
    fileInput.setAttribute("disabled", "true");
  } catch (err) {
    console.error(err);
  }
}

//---------------------------------GET DATA---------------------------

async function getData() {
  try {
    const extractAttribute = document.getElementById("extractAttribute");
    const extractAttributeName =
      extractAttribute.options[extractAttribute.selectedIndex].text;

    const url = new URL("http://localhost:5173/getData");
    url.searchParams.append("attribute", extractAttributeName);

    const response = await fetch(url);
    const data = await response.json();

    // Convert the Buffer data to a string using TextDecoder
    const textDecoder = new TextDecoder("utf-8");
    const decodedData = textDecoder.decode(new Uint8Array(data.output.data));

    const insights = document.getElementById("insights");
    insights.innerHTML = `<pre style="padding-top:50px">${decodedData}</pre>`;
  } catch (err) {
    console.error(err);
  }
}

//------------------------------SELECT GRAPH----------------------------

async function selectGraph() {
  const attributeContainer = document.getElementById("attributeContainer");

  //getting graph name
  const graph = document.getElementById("graphOptions");
  const graphName = graph.options[graph.selectedIndex].text;

  //getting the column names
  const optionResponse = await fetch("http://localhost:5173/getColumns");
  let options = await optionResponse.text();
  options = options.split(/\r?\n/).filter((value) => value.trim() !== "");

  //checking type of graph selected
  if (graphName == "Heat Map") {
    attributeContainer.innerHTML = "";
  } else if (
    graphName == "Histogram" ||
    graphName == "Box Plot" ||
    graphName == "Pie Chart"
  ) {
    //clearing so it doesnt pile up
    attributeContainer.innerHTML = "";

    const attributeSelectX = document.createElement("select");
    attributeSelectX.setAttribute("id", "attributeSelectX");
    attributeSelectX.setAttribute("style", `margin: 10px`);

    attributeContainer.appendChild(attributeSelectX);

    for (let i = 0; i < options.length; i++) {
      const option = document.createElement("option");
      option.setAttribute("value", `${option[i + 1]}`);
      option.innerHTML = options[i];
      attributeSelectX.appendChild(option);
    }
  } else {
    attributeContainer.innerHTML = "";

    const attributeSelectX = document.createElement("select");
    attributeSelectX.setAttribute("id", "attributeSelectX");
    attributeSelectX.setAttribute("style", `margin: 10px`);

    attributeContainer.appendChild(attributeSelectX);

    for (let i = 0; i < options.length; i++) {
      const option = document.createElement("option");
      option.setAttribute("value", `${option[i + 1]}`);
      option.innerHTML = options[i];
      attributeSelectX.appendChild(option);
    }

    const attributeSelectY = document.createElement("select");
    attributeSelectY.setAttribute("id", "attributeSelectY");
    attributeSelectY.setAttribute("style", `margin: 10px`);

    attributeContainer.appendChild(attributeSelectY);

    for (let i = 0; i < options.length; i++) {
      const option = document.createElement("option");
      option.setAttribute("value", `${option[i + 1]}`);
      option.innerHTML = options[i];
      attributeSelectY.appendChild(option);
    }
  }
}

//----------------------------GENERATE GRAPH--------------------------

async function generateGraph() {
  const generateButton = document.getElementById("generateButton");
  generateButton.style.visibility = "hidden";
  const graphContainer = document.getElementById("graphContainer");

  // clearing so it doesn't pile up
  graphContainer.innerHTML = "";

  // getting the graph, x, and y elements
  const graph = document.getElementById("graphOptions");
  const xElement = document.getElementById("attributeSelectX");
  const yElement = document.getElementById("attributeSelectY");

  //getting x and y values
  const url = new URL("http://localhost:5173/getGraph");
  const graphName = graph.options[graph.selectedIndex].text;
  let x;
  let y;

  // validation for y
  if (yElement) {
    y = yElement.options[yElement.selectedIndex].text;

    if (y) {
      url.searchParams.append("y", y);
    }
  }

  // validation for x
  if (xElement) {
    x = xElement.options[xElement.selectedIndex].text;
    if (x) {
      url.searchParams.append("x", x);
    }
  }
  //  console.log(x)
  //  console.log(y)

  // appending x as a query parameter
  url.searchParams.append("graph", graphName);

  let responseText;
  // fetching path
  try {
    const response = await fetch(url.toString(), {
      method: "POST",
      body: JSON.stringify({ x, y }),
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (!response.ok) {
      console.error("Error fetching graph data:", response.statusText);
      return;
    }

    responseText = await response.text();
    const path = JSON.parse(responseText);

    if (!path || !path.path || !path.path.data) {
      console.error("Invalid response format. Expected structure not found.");
      console.error("Response text:", responseText);
      return;
    }

    // decoding path
    const textDecoder = new TextDecoder("utf-8");
    const decodedPath = textDecoder.decode(new Uint8Array(path.path.data));
    //console.log(decodedPath);

    // adding image
    const image = document.createElement("img");
    image.setAttribute("src", decodedPath);
    graphContainer.appendChild(image);
    generateButton.style.visibility = "visible";
  } catch (error) {
    console.error("Error fetching graph data:", error);

    if (responseText) {
      console.error("Response text:", responseText);
    }
  }
}

//------------------------------RESET-----------------------------------

async function resetForm() {
  document.getElementById("fileInput").removeAttribute("disabled");

  const form = document.getElementById("fileUploadForm");
  form.reset();

  document.getElementById("extractAttributeContainer").innerHTML =
    "No csv file uploaded";
  document.getElementById("insights").innerHTML = "";
  document.getElementById("graphSelect").innerHTML = "No csv file uploaded";
  document.getElementById("graphContainer").innerHTML = "";

  try {
    const url = new URL(`http://localhost:5173/reset`);
    const response = await fetch(url);

    if (!response.ok) {
      console.error(`Error resetting file: ${response.statusText}`);
      return;
    }
    const reply = await response.text();
    console.log(reply);
  } catch (err) {
    console.error(err);
  }
}

window.addEventListener("beforeunload", resetForm);
