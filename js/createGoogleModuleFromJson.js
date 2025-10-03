// https://script.google.com/home

const folderId = "1R2gG0ztLSSTEjDdTrjFFlTi_FThPUtaM";
const url = "https://raw.githubusercontent.com/aphd/informatica-1/refs/heads/main/json/AI-Prompting.json";

const fetchJson = () => JSON.parse(UrlFetchApp.fetch(url).getContentText());

const getFolderById = () => DriveApp.getFolderById(folderId);

const createQuizFormInFolder = (folder, name) => {
    const form = FormApp.create(name).setIsQuiz(true); // Make the form a quiz
    DriveApp.getFileById(form.getId()).moveTo(folder);
    return form;
};

// Create choices for a question, marking the correct answer
const createChoices = (item, options, answer) => {
    const correctIndex = options.indexOf(answer);
    return options.map((opt, i) => item.createChoice(opt, i === correctIndex));
};

// Create a form item for a question
const createQuestionItem = (form, question) => {
    const item = form.addMultipleChoiceItem();
    item.setTitle(question.question).setRequired(true);
    const choices = createChoices(item, question.options, question.answer);
    item.setChoices(choices);
    return item;
};

// Populate the form with all questions
const populateQuizForm = (form, data) => {
    const items = data.questions.map((q) => createQuestionItem(form, q));
    return items;
};

const createQuizFormFromJsonUrl = () => {
    const data = fetchJson();
    const folder = getFolderById();
    const form = createQuizFormInFolder(folder, data.title || "MyQuizForm");
    populateQuizForm(form, data);
    Logger.log("Form edit URL: " + form.getEditUrl());
    Logger.log("Form stored in folder: " + folder.getName() + " (" + folder.getUrl() + ")");
    return form.getEditUrl();
};

// Run the function to create the quiz form
createQuizFormFromJsonUrl();
