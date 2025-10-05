// https://script.google.com/home

const folderId = "1R2gG0ztLSSTEjDdTrjFFlTi_FThPUtaM";
const url = "https://raw.githubusercontent.com/aphd/informatica-1/refs/heads/main/json/AI-Prompting.json";
const MAX_QUESTIONS = 2;

// Fetch JSON from URL
const fetchJson = () => JSON.parse(UrlFetchApp.fetch(url).getContentText());

// Get folder by ID
const getFolderById = () => DriveApp.getFolderById(folderId);

// Create a quiz form inside the folder
const createQuizFormInFolder = (folder, name) => {
    const form = FormApp.create(name).setIsQuiz(true); // Make it a quiz
    DriveApp.getFileById(form.getId()).moveTo(folder);
    form.setAcceptingResponses(true);
    form.setCollectEmail(false);
    form.setLimitOneResponsePerUser(false);

    // Optional: create response spreadsheet
    const ss = SpreadsheetApp.create(`${name} Responses`);
    form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());

    return form;
};

// Create multiple-choice choices with correct answer
const createChoices = (item, options, answer) => {
    const correctIndex = options.indexOf(answer);
    return options.map((opt, i) => item.createChoice(opt, i === correctIndex));
};

// Create a required multiple-choice question with points
const createQuestionItem = (form, question) => {
    const item = form.addMultipleChoiceItem();
    item.setTitle(question.question)
        .setRequired(true)   // Make sure it's required
        .setPoints(1);       // Assign 1 point by default
    const choices = createChoices(item, question.options, question.answer);
    item.setChoices(choices);
    return item;
};

// Populate form with all questions
const populateQuizForm = (form, data) => {
    const questions = data.questions.slice(0, MAX_QUESTIONS); 
    return questions.map((q) => createQuestionItem(form, q));
};

// Main function: create quiz from JSON
const createQuizFormFromJsonUrl = () => {
    const data = fetchJson();
    const folder = getFolderById();
    const form = createQuizFormInFolder(folder, data.title || "MyQuizForm");
    populateQuizForm(form, data);

    Logger.log("Form edit URL: " + form.getEditUrl());
    Logger.log("Form response spreadsheet: " + form.getDestinationId());
    Logger.log("Form stored in folder: " + folder.getName() + " (" + folder.getUrl() + ")");

    return form.getEditUrl();
};

// Run the function
createQuizFormFromJsonUrl();
