/*/
Name: Ashton Dennis
Dates: Nov 11, 2024 - 
Desc: 
/*/

// Define Constants
const SITE_EVEN = 80;
const SITE_ODD = 120;
const ALT_MEMBER_RATE = 5;
const SITE_CLEANING = 50;
const VIDEO_SURVEILLANCE = 35;
const HST = 0.15;
const STANDARD_RATE = 75;
const EXECUTIVE_RATE = 150;
const PROCESSING_FEE = 59.99;
const CANCELLATION_RATE = 0.6;

// Define Formats
const currency2Format = new Intl.NumberFormat("en-CA", {
    style: "currency",
    currency: "CAD",
    minimumFractionDigits: "2",
    maximumFractionDigits: "2",
});

// Inputs
let curDate = prompt("Current Date", "2024-04-25");

let siteNum = parseInt(prompt("Site Number (1 - 100)", "2"), 10);
let memName = prompt("Member Name", "Walter White");
let streetAdd = prompt("Member Street Address", "308 Negra Arroyo Lane");
let city = prompt("Member City", "Albuquerque");
let province = prompt("Member Province", "NM");
let postal = prompt("Member Postal Code", "A1B2C3");
let phone = prompt("Member Phone Number", "(555) 555-5555");
let mobile = prompt("Member Cell Phone Number", "(123) 123-1234");
let memType = prompt("Membership Type (S or E)", "S");
let altMembers = parseInt(prompt("Number of Alternate Members", "2"), 10);
let siteClean = prompt("Weekly Site Cleaning (Y or N)", "Y");
let videoSurveil = prompt("Video Surveillance (Y or N)", "Y");

//Calculations
let siteCost = siteNum % 2 == 0 ? SITE_EVEN : SITE_ODD; // NOT EVEN JS CAN ESCAPE MY ONE-LINERS
let altMemCost = ALT_MEMBER_RATE * altMembers;
let siteCharges = siteCost + altMemCost;

let extraCharges = 0; // Calculate extra charges and format siteClean & videoSurveil
if (siteClean == "Y") {
    siteClean = "Yes";
    extraCharges += SITE_CLEANING;
} else {
    siteClean = "No";
}
if (videoSurveil == "Y") {
    videoSurveil = "Yes";
    extraCharges += VIDEO_SURVEILLANCE;
} else {
    videoSurveil = "No";
}

let subtotal = siteCharges + extraCharges;
let taxes = subtotal * HST;
let totalMonthlyCharges = subtotal + taxes;

if (memType == "S") {
    // Determine monthly dues and format memType
    monthlyDues = STANDARD_RATE;
    memType = "Standard";
} else {
    monthlyDues = EXECUTIVE_RATE;
    memType = "Executive";
}

totalMonthlyFees = totalMonthlyCharges + monthlyDues;
totalYearlyFees = totalMonthlyFees * 12;
monthlyPayment = (totalYearlyFees + PROCESSING_FEE) / 12;
yearlySiteCharges = siteCharges * 12;
cancellationFee = yearlySiteCharges * CANCELLATION_RATE;

// Outputs

document.write(`
    <table>
        <section>
            <tr>
                <th colspan="2" class="centertext">
                    St. John's Marina & Yacht Club<br />Yearly Member
                    Receipt
                </th>
            </tr>
        </section>

        <section>
            <tr>
                <td colspan="2">
                    Client Name and Address:
                    <br />
                    <br />
                    <hr />
                    ${memName} <br />
                    ${streetAdd} <br />
                    ${city}, ${province} ${postal}<br /><br />
                    Phone: ${phone} (H) <br />
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;${mobile} (C)
                </td>
            </tr>
        </section>

        <section>
            <tr>
                <td class="middleleft">Site #: ${siteNum}</td>
                <td class="middleright">Member type: ${memType}</td>
            </tr>
            <tr>
                <td class="topleft">Alternate members:</td>
                <td class="topright righttext">${altMembers}</td>
            </tr>
            <tr>
                <td class="middleleft">Weekly site cleaning:</td>
                <td class="middleright righttext">${siteClean}</td>
            </tr>
            <tr>
                <td class="bottomleft">Video surveillance</td>
                <td class="bottomright righttext">${videoSurveil}</td>
            </tr>
        </section>

        <section>
            <tr>
                <td class="topleft">Site Charges:</td>
                <td class="topright righttext">${currency2Format.format(
                    siteCharges
                )}</td>
            </tr>
            <tr>
                <td class="bottomleft">Extra Charges:</td>
                <td class="bottomright righttext">${currency2Format.format(
                    extraCharges
                )}</td>
            </tr>
        </section>

        <section>
            <tr>
                <td class="topleft">Subtotal:</td>
                <td class="topright righttext">${currency2Format.format(
                    subtotal
                )}</td>
            </tr>
            <tr>
                <td class="bottomleft">Sales tax (HST):</td>
                <td class="bottomright righttext">${currency2Format.format(
                    taxes
                )}</td>
            </tr>
        </section>

        <section>
            <tr>
                <td class="topleft">Total monthly charges:</td>
                <td class="topright righttext">${currency2Format.format(
                    totalMonthlyCharges
                )}</td>
            </tr>
            <tr>
                <td class="bottomleft">Monthly dues:</td>
                <td class="bottomright righttext">${currency2Format.format(
                    monthlyDues
                )}</td>
            </tr>
        </section>

        <section>
            <tr>
                <td class="topleft">Total monthly fees:</td>
                <td class="topright righttext">${currency2Format.format(
                    totalMonthlyFees
                )}</td>
            </tr>
            <tr>
                <td class="bottomleft">Total yearly fees:</td>
                <td class="bottomright righttext">${currency2Format.format(
                    totalYearlyFees
                )}</td>
            </tr>
        </section>

        <section>
            <tr>
                <td class="topleft">Monthly payment:</td>
                <td class="topright righttext">${currency2Format.format(
                    monthlyPayment
                )}</td>
            </tr>
            <tr>
                <td colspan="2" class="middleleft middleright">
                    <hr />
                </td>
            </tr>
            <tr>
                <td class="middleleft">Issued:</td>
                <td class="middleright righttext">${curDate}</td>
            </tr>
            <tr>
                <td class="middleleft">HST Reg No:</td>
                <td class="middleright righttext">549-33-5849-47</td>
            </tr>
            <tr>
                <td class="bottomleft">Cancellation fee:</td>
                <td class="bottomright righttext">${currency2Format.format(
                    cancellationFee
                )}</td>
            </tr>
        </section>

        <section>
            <tr>
                <td colspan="2" class="blackbg"><br /></td>
            </tr>
        </section>
    </table>
`);
