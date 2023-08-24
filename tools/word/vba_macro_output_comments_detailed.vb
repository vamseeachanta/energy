Public Sub ExtractCommentsToNewDoc()

'Macro created 2007 by Lene Fredborg, DocTools
'The macro creates a new document
'and extracts all comments from the active document
'incl. metadata

'Minor adjustments are made to the styles used
'You may need to change the style settings and table layout to fit your needs
' http://www.vbaexpress.com/forum/showthread.php?42352-Comment-extraction-to-include-sections-as-well-as-page-numbers
'=========================

Dim oDoc As Document
Dim oNewDoc As Document
Dim oTable As Table
Dim nCount As Long
Dim n As Long
Dim Title As String

Title = "Extract All Comments to New Document"
Set oDoc = ActiveDocument
nCount = ActiveDocument.Comments.Count

If nCount = 0 Then
MsgBox "The active document contains no comments.", vbOKOnly, Title
GoTo ExitHere
Else
'Stop if user does not click Yes
If MsgBox("Do you want to extract all comments to a new document?", _
vbYesNo + vbQuestion, Title) <> vbYes Then
GoTo ExitHere
End If
End If

Application.ScreenUpdating = False
'Create a new document for the comments, base on Normal.dot
Set oNewDoc = Documents.Add
'Set to landscape
oNewDoc.PageSetup.Orientation = wdOrientLandscape
'Insert a 4-column table for the comments
With oNewDoc
.Content = ""
Set oTable = .Tables.Add _
(Range:=Selection.Range, _
numrows:=nCount + 1, _
NumColumns:=4)
End With

'Insert info in header - change date format as you wish
oNewDoc.Sections(1).Headers(wdHeaderFooterPrimary).Range.Text = _
"Comments extracted from: " & oDoc.FullName & vbCr & _
"Created by: " & Application.UserName & vbCr & _
"Creation date: " & Format(Date, "MMMM d, yyyy")

'Adjust the Normal style and Header style
With oNewDoc.Styles(wdStyleNormal)
.Font.Name = "Arial"
.Font.Size = 10
.ParagraphFormat.LeftIndent = 0
.ParagraphFormat.SpaceAfter = 6
End With

With oNewDoc.Styles(wdStyleHeader)
.Font.Size = 8
.ParagraphFormat.SpaceAfter = 0
End With

'Format the table appropriately
With oTable
.Range.Style = wdStyleNormal
.AllowAutoFit = False
.PreferredWidthType = wdPreferredWidthPercent
.PreferredWidth = 100
.Columns(1).PreferredWidth = 5
.Columns(2).PreferredWidth = 25
.Columns(3).PreferredWidth = 50
.Columns(4).PreferredWidth = 20
.Rows(1).HeadingFormat = True
End With

'Insert table headings
With oTable.Rows(1)
.Range.Font.Bold = True
.Cells(1).Range.Text = "Page"
.Cells(2).Range.Text = "Comment scope"
.Cells(3).Range.Text = "Comment text"
.Cells(4).Range.Text = "Author"
End With

'Get info from each comment from oDoc and insert in table
For n = 1 To nCount
With oTable.Rows(n + 1)
'Page number
.Cells(1).Range.Text = _
oDoc.Comments(n).Scope.Information(wdActiveEndPageNumber)
'The text marked by the comment
.Cells(2).Range.Text = oDoc.Comments(n).Scope
'The comment itself
.Cells(3).Range.Text = oDoc.Comments(n).Range.Text
'The comment author
.Cells(4).Range.Text = oDoc.Comments(n).Author
End With
Next n

Application.ScreenUpdating = True
Application.ScreenRefresh

oNewDoc.Activate
MsgBox nCount & " comments found. Finished creating comments document.", vbOKOnly, Title

ExitHere:
Set oDoc = Nothing
Set oNewDoc = Nothing
Set oTable = Nothing

End Sub