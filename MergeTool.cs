using Microsoft.TeamFoundation.VersionControl.Client;
using Microsoft.VisualStudio.Shell;
using System;

namespace MergeToolExtension
{
    public class MergeTool
    {
        public void PerformMerge(string sourceBranch, string targetBranch)
        {
            var versionControlServer = GetVersionControlServer();
            var workspace = versionControlServer.GetWorkspace(Environment.MachineName, versionControlServer.AuthorizedUser);

            var mergeResult = workspace.Merge(
                sourceBranch,
                targetBranch,
                null,
                null,
                LockLevel.None,
                RecursionType.Full,
                MergeOptions.None);

            if (mergeResult.NumConflicts > 0)
            {
                // Konfliktbehandlung
                Console.WriteLine("Merge-Konflikte gefunden.");
            }
            else
            {
                Console.WriteLine("Merge erfolgreich.");
            }
        }

        private VersionControlServer GetVersionControlServer()
        {
            var dte = (EnvDTE.DTE)Package.GetGlobalService(typeof(EnvDTE.DTE));
            var serviceProvider = new ServiceProvider(dte as Microsoft.VisualStudio.OLE.Interop.IServiceProvider);
            var tfs = (TeamFoundationServerExt)serviceProvider.GetService(typeof(TeamFoundationServerExt));
            return tfs.GetService<VersionControlServer>();
        }
    }
}
