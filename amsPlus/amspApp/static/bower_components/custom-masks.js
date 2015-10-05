$(document).ready(function () {
    $('.amfdecimalnum').inputmask("decimal",{
         radixPoint:"."
     });
    $('.amftxtnum').inputmask();
    $('.amftime').inputmask('99:99');
    $('.amftimepreiod').inputmask('از 99:99 تا 99:99');

    $('.amfdate').inputmask('d/m/9999');
    $('.amfdateperiod').inputmask('از d/m/9999 تا d/m/9999');

    $('.amfdatetime').inputmask('d/m/9999 99:99');
    $('.amfdatetimeperiod').inputmask('از d/m/9999 99:99 تا d/m/9999 99:99');
    $('.amfcurrncy').inputmask("decimal",{
         radixPoint:".",
         groupSeparator: ",",
         digits: 2,
         autoGroup: true,
         prefix: 'ریال'
     });








});