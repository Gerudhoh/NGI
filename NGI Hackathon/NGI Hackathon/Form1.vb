Public Class Form1

    Dim home, info, game, contact As Boolean

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        home = True
        info = False
        game = False
        contact = False

        pbFinances.Visible = True

        pbBankBot.Visible = False
        pbBankBot1.Visible = False

        pbGame.Visible = False

        pbFacebook.Visible = False
        pbInstagram.Visible = False
        pbTwitter.Visible = False
        pbYoutube.Visible = False
        pbLinkedin.Visible = False
        pbSuggestion.Visible = False

        If home = True Then
            lblInfo.Text = "As university students ourselves, we have recognized that financial literacy is often an overlooked skill for many young adults. We are faced with a number of money management decisions and are hoping to make learning about finances more time efficient, fun and easy for youth!"
        ElseIf info = True Then
            lblInfo.Text = "Welcome to our Banking Helper Bot! We know that university students are very busy and can’t always make it to their nearest bank branch to get all of their financial questions answered. We made this process even easier for you by answering any questions you may have about financing, budgeting or financial tools from the comfort of your own home."
        ElseIf game = True Then
            lblInfo.Text = "Use our interactive game, The Cost of Life, to help plan your future! The game will ask you a few multiple choice questions to help determine the cost of your schooling- but it doesn’t stop there!! Afterwards, it will help you learn about how to save your money and the various options you have with RBC."
        ElseIf contact = True Then
            lblInfo.Text = "Any unanswered questions?                       Contact us anytime!                                        Phone: 1 (800) 769-2511"
        End If
    End Sub

    Private Sub btnHome_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnHome.Click
        home = True
        info = False
        game = False
        contact = False

        pbFinances.Visible = True

        pbBankBot.Visible = False
        pbBankBot1.Visible = False

        pbGame.Visible = False

        pbFacebook.Visible = False
        pbInstagram.Visible = False
        pbTwitter.Visible = False
        pbYoutube.Visible = False
        pbLinkedin.Visible = False
        pbSuggestion.Visible = False

        lblInfo.Text = "As university students ourselves, we have recognized that financial literacy is often an overlooked skill for many young adults. We are faced with a number of money management decisions and are hoping to make learning about finances more time efficient, fun and easy for youth!"
    End Sub

    Private Sub btnInfo_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnInfo.Click
        info = True
        home = False
        game = False
        contact = False

        pbFinances.Visible = False

        pbBankBot.Visible = True
        pbBankBot1.Visible = True

        pbGame.Visible = False

        pbFacebook.Visible = False
        pbInstagram.Visible = False
        pbTwitter.Visible = False
        pbYoutube.Visible = False
        pbLinkedin.Visible = False
        pbSuggestion.Visible = False

        lblInfo.Text = "Welcome to our Banking Helper Bot! We know that university students are very busy and can’t always make it to their nearest bank branch to get all of their financial questions answered. We made this process even easier for you by answering any questions you may have about financing, budgeting or financial tools from the comfort of your own home."
    End Sub

    Private Sub btnGame_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnGame.Click
        game = True
        home = False
        info = False
        contact = False

        pbFinances.Visible = False

        pbBankBot.Visible = False
        pbBankBot1.Visible = False

        pbGame.Visible = True

        pbFacebook.Visible = False
        pbInstagram.Visible = False
        pbTwitter.Visible = False
        pbYoutube.Visible = False
        pbLinkedin.Visible = False
        pbSuggestion.Visible = False

        lblInfo.Text = "Use our interactive game, The Cost of Life, to help plan your future! The game will ask you a few multiple choice questions to help determine the cost of your schooling- but it doesn’t stop there!! Afterwards, it will help you learn about how to save your money and the various options you have with RBC."
    End Sub

    Private Sub btnContact_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnContact.Click
        contact = True
        home = False
        info = False
        game = False

        pbFinances.Visible = False

        pbBankBot.Visible = False
        pbBankBot1.Visible = False

        pbGame.Visible = False

        pbFacebook.Visible = True
        pbInstagram.Visible = True
        pbTwitter.Visible = True
        pbYoutube.Visible = True
        pbLinkedin.Visible = True
        pbSuggestion.Visible = True

        lblInfo.Text = "Any unanswered questions?                       Contact us anytime!                                        Phone: 1 (800) 769-2511"
    End Sub

    Private Sub pbGame_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles pbGame.Click
        System.Diagnostics.Process.Start("http://woohyu.dev.fast.sheridanc.on.ca/Game/gameStart.html")
    End Sub

    Private Sub pbBankBot1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles pbBankBot1.Click
        System.Diagnostics.Process.Start("https://web.telegram.org/#/im?p=@NGI_G12_bot")
    End Sub
End Class
