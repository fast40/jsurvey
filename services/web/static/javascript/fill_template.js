const QUESTION_NUMBER = 1;  // <- Change this to set the question number

const initial_answer_field = "initial_answer" + QUESTION_NUMBER + "_";  // e.g. initial_answer1_1 (last digit is set later)
const meta_error_field = "meta_error" + QUESTION_NUMBER + "_";  // e.g. meta_error1_1 (last digit is set later)

const xhttp = new XMLHttpRequest;

xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    const server_response = JSON.parse(xhttp.responseText);
    
    for (var i = 0; i < server_response['initial_answers'].length; i++) {
      const initial_answer_element = document.getElementById("initial_answer_" + (i + 1));
      const meta_error_element = document.getElementById("meta_error_" + (i + 1));

      const initial_answer = server_response["initial_answers"][i];
      const meta_error = server_response["meta_errors"][i];
      
      if (initial_answer_element != null) {
        Qualtrics.SurveyEngine.setEmbeddedData(initial_answer_field + (i + 1), initial_answer);
        initial_answer_element.innerHTML = initial_answer;
      }

      if (meta_error_element != null) {
        Qualtrics.SurveyEngine.setEmbeddedData(meta_error_field + (i + 1), meta_error);
        meta_error_element.innerHTML = meta_error;
      }
    }
  }
}

xhttp.open("GET", "https://c1.elifast.com/get_responses?question_number=" + QUESTION_NUMBER);
xhttp.send();