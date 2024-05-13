const policyText = document.getElementById('policy-text');
const acceptanceCheckbox = document.getElementById('acceptance-checkbox');
const submitButton = document.getElementById('submit-button');

submitButton.addEventListener('click', () => {
    if (acceptanceCheckbox.checked) {
        // Submit the user's acceptance to the Lambda function
        // Replace with your actual Lambda function invocation code
        console.log('User has accepted the data privacy policy.');
    } else {
        alert('Please accept the data privacy policy to continue.');
    }
});

// Load the data privacy policy text from an external file or API call
fetch('data-privacy-policy.txt')
    .then(response => response.text())
    .then(text => policyText.innerHTML = text);
