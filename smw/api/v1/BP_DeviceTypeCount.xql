xquery version "3.0";
declare namespace mlhim2="http://www.mlhim.org/xmlns/mlhim2/2_4_1";
let $title := "BP Device Type Counts"
let $vitals := collection("/db/apps/mlhim-emr/data/care")//mlhim2:el-a2bc25db-3111-4cd5-9825-d9c448cdd1a4
  let $total := count($vitals)
  let $macnt := count($vitals//mlhim2:el-7ecfdbba-e863-4417-a41c-a09f035d2a2c[contains(mlhim2:DvString-dv,"Manual Analog")])
  let $aacnt := count($vitals//mlhim2:el-7ecfdbba-e863-4417-a41c-a09f035d2a2c[contains(mlhim2:DvString-dv,"Automatic Analog")])
  let $digcnt := count($vitals//mlhim2:el-7ecfdbba-e863-4417-a41c-a09f035d2a2c[contains(mlhim2:DvString-dv,"Digital")])

return
      <results>
      <ReportTitle>{$title}</ReportTitle>
      <ManualAnalog>{$aacnt}</ManualAnalog>
      <AutomaticAnalog>{$aacnt}</AutomaticAnalog>
      <Digtal>{$digcnt}</Digtal>
      <Total>{$total}</Total>
      </results>