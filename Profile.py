import flet as ft
import os

def main(page: ft.Page):
    page.title = "Swiper's Netlify Dashboard"
    page.vertical_alignment = ft.CrossAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 800
    page.window_height = 700
    page.window_resizable = True
    page.theme_mode = ft.ThemeMode.DARK # A cool dark theme

    # --- State Variables ---
    selected_pfp_path = ft.Ref[ft.Text]()
    pfp_image = ft.Ref[ft.Image]()
    selected_deploy_folder = ft.Ref[ft.Text]()

    # --- Event Handlers ---

    def pick_pfp_result(e: ft.FilePickerResultEvent):
        if e.files:
            pfp_path = e.files[0].path
            pfp_image.current.src = pfp_path
            selected_pfp_path.current.value = f"Selected: {os.path.basename(pfp_path)}"
            page.update()

    def pick_deploy_folder_result(e: ft.FilePickerResultEvent):
        if e.path:
            selected_deploy_folder.current.value = f"Folder: {e.path}"
            page.update()

    def deploy_to_netlify(e):
        folder_to_deploy = selected_deploy_folder.current.value
        if folder_to_deploy and "Folder: " in folder_to_deploy:
            folder_path = folder_to_deploy.replace("Folder: ", "")
            # In a real application, you would execute the Netlify CLI here.
            # Example (requires Netlify CLI installed and configured):
            # import subprocess
            # try:
            #     # This assumes you have 'netlify-cli' installed globally or in your PATH
            #     # and are logged in. 'netlify deploy --prod --dir <folder_path>'
            #     # For a simple draft deploy:
            #     # result = subprocess.run(['netlify', 'deploy', '--dir', folder_path], capture_output=True, text=True, check=True)
            #     # For a production deploy:
            #     # result = subprocess.run(['netlify', 'deploy', '--prod', '--dir', folder_path], capture_output=True, text=True, check=True)
            #     # print(result.stdout)
            #     # print(result.stderr)
            #     page.snack_bar = ft.SnackBar(
            #         ft.Text(f"Attempting to deploy '{folder_path}' to Netlify... (Check console for details)"),
            #         open=True
            #     )
            # except Exception as ex:
            #     page.snack_bar = ft.SnackBar(
            #         ft.Text(f"Deployment failed: {ex}"),
            #         open=True
            #     )
            page.snack_bar = ft.SnackBar(
                ft.Text(f"Simulating deployment of '{folder_path}' to Netlify. (Actual deployment requires Netlify CLI)"),
                open=True
            )
        else:
            page.snack_bar = ft.SnackBar(
                ft.Text("Please select a folder to deploy first."),
                open=True
            )
        page.update()

    # --- File Pickers ---
    file_picker_pfp = ft.FilePicker(on_result=pick_pfp_result)
    file_picker_deploy_folder = ft.FilePicker(on_result=pick_deploy_folder_result)

    # Add file pickers to the page's overlay
    page.overlay.append(file_picker_pfp)
    page.overlay.append(file_picker_deploy_folder)

    # --- UI Layout ---
    page.add(
        ft.AppBar(
            title=ft.Text("Swiper's Netlify Dashboard", weight=ft.FontWeight.BOLD),
            center_title=True,
            bgcolor=ft.colors.BLUE_GREY_900,
        ),
        ft.Container(
            content=ft.Column(
                [
                    # User Profile Section
                    ft.Card(
                        elevation=10,
                        content=ft.Container(
                            padding=20,
                            content=ft.Column(
                                [
                                    ft.Text("User Profile", size=20, weight=ft.FontWeight.BOLD),
                                    ft.Divider(),
                                    ft.Row(
                                        [
                                            ft.Column(
                                                [
                                                    ft.Text(f"Username: Swiper", size=16),
                                                    ft.Text(f"Scripting Language: C++", size=16),
                                                ],
                                                alignment=ft.MainAxisAlignment.START,
                                                horizontal_alignment=ft.CrossAxisAlignment.START,
                                                expand=True
                                            ),
                                            ft.Column(
                                                [
                                                    ft.CircleAvatar(
                                                        radius=50,
                                                        foreground_image_url="https://via.placeholder.com/100/0000FF/FFFFFF?text=PFP", # Default placeholder
                                                        content=ft.Image(
                                                            ref=pfp_image,
                                                            src="https://via.placeholder.com/100/0000FF/FFFFFF?text=PFP", # Default placeholder
                                                            fit=ft.ImageFit.COVER,
                                                            border_radius=ft.border_radius.all(50)
                                                        )
                                                    ),
                                                    ft.ElevatedButton(
                                                        "Choose PFP",
                                                        icon=ft.icons.UPLOAD_FILE,
                                                        on_click=lambda _: file_picker_pfp.pick_files(
                                                            allow_multiple=False,
                                                            allowed_extensions=["jpg", "jpeg", "png", "gif"]
                                                        ),
                                                        style=ft.ButtonStyle(
                                                            shape=ft.RoundedRectangleBorder(radius=5),
                                                            bgcolor=ft.colors.BLUE_GREY_700,
                                                            color=ft.colors.WHITE
                                                        )
                                                    ),
                                                    ft.Text(ref=selected_pfp_path, value="No PFP selected", size=12, italic=True)
                                                ],
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER
                                    )
                                ]
                            )
                        ),
                        width=600,
                        margin=ft.margin.only(bottom=20)
                    ),

                    # Friends List Section
                    ft.Card(
                        elevation=10,
                        content=ft.Container(
                            padding=20,
                            content=ft.Column(
                                [
                                    ft.Text("Friends", size=20, weight=ft.FontWeight.BOLD),
                                    ft.Divider(),
                                    ft.Column(
                                        [
                                            ft.ListTile(leading=ft.Icon(ft.icons.PERSON), title=ft.Text("Screamingcat")),
                                            ft.ListTile(leading=ft.Icon(ft.icons.PERSON), title=ft.Text("Popcat")),
                                            ft.ListTile(leading=ft.Icon(ft.icons.PERSON), title=ft.Text("Zen")),
                                            ft.ListTile(leading=ft.Icon(ft.icons.PERSON), title=ft.Text("Foot_Licker")),
                                            ft.ListTile(leading=ft.Icon(ft.icons.PERSON), title=ft.Text("W1NGZ")),
                                        ],
                                        spacing=0
                                    )
                                ]
                            )
                        ),
                        width=600,
                        margin=ft.margin.only(bottom=20)
                    ),

                    # Netlify Deployment Section
                    ft.Card(
                        elevation=10,
                        content=ft.Container(
                            padding=20,
                            content=ft.Column(
                                [
                                    ft.Text("Netlify Deployment", size=20, weight=ft.FontWeight.BOLD),
                                    ft.Divider(),
                                    ft.Text("Select a folder to deploy to Netlify:", size=16),
                                    ft.Row(
                                        [
                                            ft.ElevatedButton(
                                                "Select Folder",
                                                icon=ft.icons.FOLDER_OPEN,
                                                on_click=lambda _: file_picker_deploy_folder.get_directory_path(),
                                                style=ft.ButtonStyle(
                                                    shape=ft.RoundedRectangleBorder(radius=5),
                                                    bgcolor=ft.colors.BLUE_GREY_700,
                                                    color=ft.colors.WHITE
                                                )
                                            ),
                                            ft.Text(ref=selected_deploy_folder, value="No folder selected", expand=True, italic=True)
                                        ],
                                        alignment=ft.MainAxisAlignment.START,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER
                                    ),
                                    ft.ElevatedButton(
                                        "Deploy to Netlify",
                                        icon=ft.icons.CLOUD_UPLOAD,
                                        on_click=deploy_to_netlify,
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=5),
                                            bgcolor=ft.colors.GREEN_700,
                                            color=ft.colors.WHITE
                                        ),
                                        width=200,
                                        height=40
                                    ),
                                    ft.Text(
                                        "Note: Actual deployment requires Netlify CLI installed and configured.",
                                        size=12,
                                        color=ft.colors.GREY_500,
                                        italic=True
                                    )
                                ]
                            )
                        ),
                        width=600
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                scroll=ft.ScrollMode.ADAPTIVE # Enable scrolling if content overflows
            ),
            padding=20,
            expand=True
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
