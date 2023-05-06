function customtag() {
    let CustomMessage1;
    let CustomMessage2;
    let CustomMessage3;
    let finString;

    if (Progress() > 50) {
        finString = CustomMessage1;
    } else if (Progress() > 85) {
        finString = CustomMessage2;
    } else if (Progress() > 100) {
        finString = CustomMessage3;
    }

    return `${finString}`
}
RegisterTag('', customtag, true)